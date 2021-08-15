from django.shortcuts import render

def index (request):
    diction={}
    return render(request, 'frontend/index.html', context=diction)


def about (request):
    diction={}
    return render(request, 'frontend/about.html', context=diction)

def faq (request):
    diction={}
    return render(request, 'frontend/faq.html', context=diction)

def plans (request):
    diction={}
    return render(request, 'frontend/plans.html', context=diction)

def support (request):
    diction={}
    return render(request, 'frontend/support.html', context=diction)

def terms (request):
    diction={}
    return render(request, 'frontend/terms.html', context=diction)
