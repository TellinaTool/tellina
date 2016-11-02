from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import NLRequest, Translation

def about(request):
    return HttpResponse("coming soon...")

def explain(request):
    return render(request, 'translator/explain.html', {})

def index(request):
    latest_request_list = NLRequest.objects.order_by('-sub_time')[:10]
    template = loader.get_template('translator/index.html')
    context = {
        'latest_request_list': latest_request_list,
    }
    return HttpResponse(template.render(context, request))