from django.shortcuts import render

def home(request):
    context = {
        'title' : 'citizen should be the title'
    }
    return render(request, 'base.html', context)

def citizen(request):
    context = {
        'title' : 'citizen'
    }
    return render(request, 'citizen/index.html', context)

def ntv(request):
    context = {
        'title' : 'ntv'
    }
    return render(request, 'ntv/index.html', context)

def ktn_news(request):
    context = {
        'title' : 'ktn news'
    }
    return render(request, 'ktn_news/index.html', context)

def k24(request):
    context = {
        'title' : 'k24'
    }
    return render(request, 'k24/index.html', context)
