from django.db import models
from django.urls import reverse

class Store(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('storeItem', kwargs={'storeItem_slug': self.slug})
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id', 'time_create', 'title']

class Category(models.Model):
    #название категории связанной таблицы с инексацией для ускорения поиска
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    #метод для возврата имя категории
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('storeCat', kwargs={'storeCat_slug': self.slug})
    #Для вывода в админ панели
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['id']