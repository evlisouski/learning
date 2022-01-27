from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(response):
    return HttpResponse('Страница приложения women.')

def categories(request, catid):
    return HttpResponse(f"<h1> Статьи по категориям {catid}")

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')