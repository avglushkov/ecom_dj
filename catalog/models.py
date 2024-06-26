from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование категории')
    category_description = models.CharField(max_length=500, verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания (записи в БД)')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения (записи в БД)')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя контакта')
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='Телефон')
    email = models.CharField(max_length=50, blank=True, null=True, verbose_name='Почта')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name


class Blog(models.Model):
    header = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(blank=True, null=True, max_length=100, verbose_name='Ссылка')
    content = models.TextField(blank=True, null=True, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blogs/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    published = models.BooleanField(default=False, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Счетчик просмотров')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return f'{self.header}'
