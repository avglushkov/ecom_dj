# Generated by Django 5.0.6 on 2024-06-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_product_manufactured_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата создания (записи в БД)'),
        ),
    ]
