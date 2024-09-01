# news/models.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django.db import models

class News(models.Model):
    title = models.CharField('Название новости', max_length=100)
    content = models.TextField("Новость")
    created_at = models.DateField(verbose_name="Дата публикации")
    author = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


    def __str__(self):
        return self.title
