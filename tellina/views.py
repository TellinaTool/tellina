from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect

from .translate import translate_fun
from .models import NLRequest, Translation

def about(request):
    return HttpResponse("coming soon...")

@csrf_protect
def translate(request):
    if request.method == 'POST':
        request_str = request.POST.get('request_str')
        if not request_str or not request_str.strip():
            return redirect('/')
        if NLRequest.objects.filter(request_str=request_str).exists():
            # request has been issued before
            nl_request = NLRequest.objects.filter(request_str=request_str)
            for nlr in nl_request:
                nlr.frequency += 1
                nlr.save()

            if Translation.objects.filter(request__request_str__equals=request_str).exists():
                # model translations exist
                translation_list = Translation.objects.filter(request__request_str__equals=request_str)
            else:
                # call learning model and store the translations
                top_k_predictions = translate_fun(request_str)


        else:
            nlr = NLRequest(request_str=request_str, frequency=1)
            nlr.save()
    return HttpResponse()

def index(request):
    latest_request_list = NLRequest.objects.order_by('-sub_time')[:10]
    template = loader.get_template('translator/index.html')
    context = {
        'latest_request_list': latest_request_list,
    }
    return HttpResponse(template.render(context, request))