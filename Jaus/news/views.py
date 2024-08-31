from django.shortcuts import render
from .models import News  # Импортируем модель новостей

def news_list(request):
    news_items = News.objects.all()  # Получаем все новости из базы данных
    return render(request, 'news/news_list.html', {'news_items': news_items})