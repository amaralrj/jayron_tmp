# coding: utf-8
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {"current_url": "home"})

def quemsomos(request):
    return render(request, 'quem-somos.html', {"current_url": "quem-somos"})
# Create your views here.
