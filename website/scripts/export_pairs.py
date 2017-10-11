import os,sys

sys.path.append(os.path.join(
    os.path.dirname(__file__), "..", "tellina_learning_module"))

from bashlint import bash, data_tools
import collections

from website.constants import *
from website.models import *

def export_pairs(output_dir):
    nl_list = []
    cm_list = []
    for annotation in Annotation.objects.all():
        nl = annotation.nl.str.strip().replace('\n', ' ')
        cm = annotation.cmd.str.strip().replace('\n', ' ')
        if nl in INVALID_ANNOTATION_TAGS:
            continue
        nl_list.append(nl)
        cm_list.append(cm)

    assert(len(nl_list) == len(cm_list))
     
    nl_path = os.path.join(output_dir, 'nl.txt')
    cm_path = os.path.join(output_dir, 'cm.txt')

    with open(nl_path, 'w') as o_f:
        for nl in nl_list:
            o_f.write('{}\n'.format(nl))
    print('{} nls saved to {}'.format(len(nl_list), nl_path))

    with open(cm_path, 'w') as o_f:
        for cm in cm_list:
            o_f.write('{}\n'.format(cm))
    print('{} cms saved to {}'.format(len(cm_list), cm_path))


def gen_annotation_check_sheet(output_dir):
    utilities_to_check = {
        'tr',
        'md5sum',
        'ssh',
        'hostname',
        'gzip',
        'ping',
        'diff',
        'rsync',
        'tee',
        'cat',
        'set',
        'ln',
        'pwd',
        'sort',
        'comm',
        'history',
        'df',
        'rename',
        'read',
        'nl',
        'cd',
        'rev',
        'zcat',
        'less',
        'which',
        'uniq',
        'dig',
        'date',
        'ps',
        'cal'
    }

    commands_by_utility = collections.defaultdict(set)
    for url in URL.objects.all():
        for command in url.commands.all():
            ast = data_tools.bash_parser(command.str)
            template = data_tools.ast2template(ast, 
                loose_constraints=True, ignore_flag_order=True)
            utilities = data_tools.get_utilities(ast)
            if utilities & bash.BLACK_LIST or utilities & bash.GREY_LIST:
                continue
            uts_to_check = utilities & utilities_to_check
            if uts_to_check:
                for utility in uts_to_check:
                    commands_by_utility[utility].add((command.str, template))

    check_assignments = {}
    with open(os.path.join(os.path.dirname(__file__), 
            'annotation_check_assignments.txt')) as f:
        for line in f:
            access_code, utilities = line.strip().split()
            check_assignments[access_code] = utilities.split(',')
            
    templates_seen = collections.defaultdict(int)
    for access_code in check_assignments:
        output_path = os.path.join(output_dir, 
            'annotation_check_sheet.{}.csv'.format(access_code))
        print('saving to {}...'.format(output_path))
        with open(output_path, 'w') as o_f:
            o_f.write('Utility,Command,Description\n')
            for utility in check_assignments[access_code]:
                print('\t{}'.format(utility))
                commands = sorted(list(commands_by_utility[utility]))
                for i, (cmd, template) in enumerate(commands):
                    utility_str = utility if i == 0 else ''
                    annotations = Annotation.objects.filter(cmd__str=cmd)
                    if annotations:
                        for annotation in annotations:
                            nl = annotation.nl.str.strip().replace('\n', ' ')
                            if nl in INVALID_ANNOTATION_TAGS:
                                continue
                            o_f.write('{},"{}","{}"\n'.format(utility_str, 
                                cmd.replace('"', '""'), nl.replace('"', '""')))
                            o_f.write(',,<Type a new description here>\n')
                    else:
                        if not template in templates_seen:
                            templates_seen[template] = 1
                            o_f.write('{},"{}","{}"\n'.format(utility_str, 
                                cmd.replace('"', '""'), '--'))   
                            o_f.write(',,<Type a new description here>\n')                 
