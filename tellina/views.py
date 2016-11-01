from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse("coming soon...")

def explain(request):
    return render(request, 'translator/explain.html', {})

def index(request):
    return render(request, 'translator/index.html', {})