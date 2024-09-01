from .models import News
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'author', 'created_at', 'content']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор новости'}),
            'created_at': DateTimeInput(format='%Y-%m-%d',attrs={'class': 'form-control', 'placeholder': 'Дата публикации'})
        }