# Generated by Django 5.0.6 on 2024-06-10 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите категорию', max_length=100, verbose_name='Категория')),
                ('description', models.TextField(blank=True, help_text='Введите описаание категории', null=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование продукта', max_length=100, verbose_name='Наименование')),
                ('description', models.CharField(help_text='Введите описаание продукта', max_length=100, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, help_text='Вставте изображение продукта', null=True, upload_to='products/photo', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за покупку')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name', 'price'],
            },
        ),
    ]
