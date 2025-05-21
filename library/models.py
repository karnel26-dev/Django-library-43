from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    published_date = models.DateField(verbose_name='Дата издания')
    isbn = models.CharField(max_length=13, blank=True, verbose_name='ISBN')
    pages = models.IntegerField(verbose_name='Количество страниц')

    def __str__(self):
        return f"{self.title} by {self.author}"
