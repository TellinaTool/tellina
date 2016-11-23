import os
import sys

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "commandline-helper"))
from tellina.models import NLRequest, Translation

DEBUG = False

from tellina.helper_interface import translate_fun


def about(request):
    return HttpResponse("coming soon...")

def mockup_translate(request):
    template = loader.get_template('mockups/translate.html')
    context = {}
    return HttpResponse(template.render(context, request))

@csrf_protect
def translate(request):
    template = loader.get_template('translator/translate.html')
    if request.method == 'POST':
        request_str = request.POST.get('request_str')
    else:
        request_str = request.GET.get('request_str')

    if not request_str or not request_str.strip():
        return redirect('/')
    translation_list = []
    if NLRequest.objects.filter(request_str=request_str).exists():
        # request has been issued before
        nl_request = NLRequest.objects.filter(request_str=request_str)
        for nlr in nl_request:
            nlr.frequency += 1
            nlr.save()
        if Translation.objects.filter(request__request_str=request_str).exists():
            # model translations exist
            translation_list = Translation.objects.filter(
                request__request_str=request_str)
    else:
        # record request
        nlr = NLRequest(request_str=request_str, frequency=1)
        nlr.save()
    if not translation_list:
        # call learning model and store the translations
        batch_outputs, output_logits = translate_fun(request_str)
        top_k_predictions = batch_outputs[0]
        top_k_scores = output_logits[0]
        for i in range(len(top_k_predictions)):
            pred_tree, pred_cmd, outputs = top_k_predictions[i]
            score = top_k_scores[i]
            trans = Translation(request=nlr, pred_cmd=pred_cmd,
                                score=score, num_votes=0)
            trans.save()
            translation_list.append(trans)

    context = {
        'nl_request': nlr,
        'translation_list': translation_list,
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def web_search(request):
    template = loader.get_template('translator/websearch.html')
    context = {}
    return HttpResponse(template.render(context, request))

def index(request):
    latest_request_list = NLRequest.objects.order_by('-sub_time')[:10]
    template = loader.get_template('translator/index.html')
    context = {
        'latest_request_list': latest_request_list,
    }
    return HttpResponse(template.render(context, request))

def task(request):
    template = loader.get_template('platform/task.html')
    context = {}
    return HttpResponse(template.render(context, request))