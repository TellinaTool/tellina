import os,sys

sys.path.append(os.path.join(
    os.path.dirname(__file__), "..", "tellina_learning_module"))

from bashlint import data_tools
import collections

from website.constants import *
from website.models import Annotation

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
    }

    examples_by_utility = collections.defaultdict(list)
    for annotation in Annotation.objects.all():
        nl = annotation.nl.str.strip().replace('\n', ' ')
        cm = annotation.cmd.str.strip().replace('\n', ' ')
        if nl in INVALID_ANNOTATION_TAGS:
            continue
        ast = data_tools.bash_parser(cm)
        utilities = data_tools.get_utilities(ast)
        if utilities & utilities_to_check:
            for utility in utilities:
                examples_by_utility[utility].append(cm, nl)

    with open(os.path.join(output_dir, 'annotation_check_sheet.csv'), 'w') as o_f:
        o_f.write('utility,command,description,fixed description')
        for utility in utilities_to_check:
            examples = examples_by_utility[utility]
            for cm, nl in examples:
                o_f.write('{},{},{}\n'.format(utility,cm,nl))