from website.models import Annotation

nl_list = []
cm_list = []
for annotation in Annotation.objects.all():
    nl_list.append(annotation.nl.str)
    cm_list.append(annotation.cmd.str)

with open('nl.txt', 'w') as o_f:
    for nl in nl_list:
        o_f.write('{}\n'.format(nl.strip()))

with open('cm.txt', 'w') as o_f:
    for cm in cm_list:
        o_f.write('{}\n'.format(cm.strip()))