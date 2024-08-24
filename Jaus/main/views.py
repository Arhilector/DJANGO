from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый джанго проект!</h1>")


def new(request):
    return HttpResponse("<h1>'это вторая страница моего проекта на джанго'</h1>")

def data(request):
    return HttpResponse("<h1>'Это оригинальный текст для страницы data'</h1>")

def test(request):
    return HttpResponse("<h1>'Это оригинальный текст для страницы test'</h1>")