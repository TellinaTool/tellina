from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from .models import NLRequest, Translation

def about(request):
    return HttpResponse("coming soon...")

def translate(request):
    if request.method == 'POST':
        request_str = request.POST.get('request_str')
        if not request_str or not request_str.strip():
            return redirect('/')
    print(request.POST)

    nl_request = NLRequest.objects.get(request_str=request_str)
    print(nl_request)
    if nl_request:
        translation_list = Translation.objects.filter(request=nl_request).all()
    else:
        pass
    context = {
        'translation_list': translation_list,
    }
    template = loader.get_template('translator/translate.html')
    return HttpResponse(template.render(context, request))

def index(request):
    latest_request_list = NLRequest.objects.order_by('-sub_time')[:10]
    template = loader.get_template('translator/index.html')
    context = {
        'latest_request_list': latest_request_list,
    }
    return HttpResponse(template.render(context, request))