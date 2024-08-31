from django.shortcuts import render
from news.models import News  # Импортируем модель новостей

def home(request):
    news_items = News.objects.all()  # Получаем все новости
    return render(request, 'main/home.html', {'news_items': news_items})  # Передаем новости в контекст

def about(request):
    return render(request, 'main/about.html')

def products(request):
    return render(request, 'main/products.html')

def contact(request):
    return render(request, 'main/contact.html')

def news_list(request):
    news_items = News.objects.all()  # Получаем все новости из базы данных
    return render(request, 'news/news_list.html', {'news_items': news_items})