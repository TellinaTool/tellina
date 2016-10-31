from django.shortcuts import render

def index(request):
    return render(request, 'translator/index.html', {})

def explain(request):
    return render(request, 'translator/explain.html', {})