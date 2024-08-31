# news/models.py

from django.contrib.auth.models import User
from django.db import models

class News(models.Model):
    title = models.CharField('Название новости', max_length=100)
    content = models.TextField("Новость")
    created_at = models.DateTimeField("Дата публикации")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор статьи", null=True, blank=True)


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


    def __str__(self):
        return self.title
