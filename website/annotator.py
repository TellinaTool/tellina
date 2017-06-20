from django.db.models import Count
from django.http import HttpResponse
from django.template import loader

from website import functions
from website.models import NL, Command, URL, User, CommandTag, URLTag, \
    Annotation, AnnotationJudgement

WHITE_LIST = {'find', 'xargs'}
BLACK_LIST = {'cpp', 'g++', 'python', 'java', 'emacs', 'vim'}

def access_code_required(f):
    @functions.wraps(f)
    def g(request, *args, **kwargs):
        try:
            access_code = request.COOKIES['access_code']
        except KeyError:
            raise Exception("No user ID!")
        return f(request, *args, access_code=access_code, **kwargs)
    return g


def url_panel(request):
    """
    Display a list of urls for a particular utility.
    """
    template = loader.get_template('annotator/url_panel.html')

    utility = request.GET.get('utility')
    print(utility)
    url_list = []
    for url_tag in URLTag.objects.filter(tag=utility).order_by('url'):
        url_list.append(url_tag.url.str)

    context = {
        'utility': utility,
        'url_list': url_list
    }
    return HttpResponse(template.render(context=context, request=request))


def utility_panel(request):
    """
    Display all the utilities to annotate.
    """
    template = loader.get_template('annotator/utility_panel.html')
    utilities = []
    for obj in URLTag.objects.values('tag').annotate(the_count=Count('tag'))\
            .order_by('-the_count'):
        if not obj['tag'] in WHITE_LIST and not obj['tag'] in BLACK_LIST:
            print(obj['the_count'])
            utilities.append(obj['tag'])

    utility_groups = []
    for i in range(0, len(utilities), 20):
        utility_group = utilities[i:i+20]
        if len(utility_group) > 10:
            utility_groups.append([utility_group[:10], utility_group[10:]])
        else:
            utility_groups.append([utility_group[:10], []])

    context = {'utility_groups': utility_groups}

    return HttpResponse(template.render(context=context, request=request))


def login(request):
    """
    User registration & login.
    """
    template = loader.get_template('annotator/login.html')
    return HttpResponse(template.render(context={}, request=request))