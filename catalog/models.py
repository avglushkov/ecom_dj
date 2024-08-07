from django.db import models
from users.models import User


# Create your models here.
class Category(models.Model):
    # objects = None
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания (записи в БД)')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения (записи в БД)')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            ('can_change_publication_status', 'can change publication status'),
            ('can_change_description', 'can change description'),
            ('can_change_category', 'can change category')
        ]

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


class Version(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Продукт')
    version_number = models.IntegerField(default=1, verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    actual_version = models.BooleanField(default=False,verbose_name='Признак текущей версии')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.version_number} - {self.version_name}'


