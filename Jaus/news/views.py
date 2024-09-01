from django.shortcuts import render, redirect
from .models import News  # Импортируем модель новостей
from .forms import NewsForm

def news_list(request):
    news_items = News.objects.all()  # Получаем все новости из базы данных
    return render(request, 'news/news_list.html', {'news_items': news_items})

def create_news(request):
    errors = ""
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базу данных
            return redirect('news_list')  # Редирект на страницу со списком новостей после успешного добавления
        else:
            errors = "Данные заполнены некорректно!"
            print(form.errors)  # Выводим ошибки формы для отладки
    else:
        form = NewsForm()  # Создаем пустую форму, если метод запроса не POST

    context = {
        'form': form,
        'errors': errors
    }
    return render(request, 'news/add_new_post.html', context)