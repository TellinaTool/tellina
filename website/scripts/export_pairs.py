import os

from website.models import Annotation

def export_pairs(output_dir):
    nl_list = []
    cm_list = []
    for annotation in Annotation.objects.all():
        nl = annotation.nl.str.strip().replace('\n', ' ')
        cm = annotation.cmd.str.strip().replace('\n', ' ')
        if nl in ['NA', 'ERROR', 'DUPLICATE', 'WRONG', 'I DON\'T KNOW']:
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
