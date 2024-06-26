# Generated by Django 5.0.2 on 2024-04-19 14:46

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'такой маршрут уже существует'}, max_length=50, unique=True, verbose_name='Название маршрута')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('route_cities', models.CharField(max_length=150, verbose_name='Города маршрута')),
                ('travel_time', models.CharField(max_length=50, verbose_name='Длительность маршрута')),
                ('base_city', models.CharField(max_length=50, verbose_name='Базовый город')),
                ('bus', models.CharField(blank=True, max_length=50, verbose_name='Общественный транспорт')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Описание')),
                ('image', models.ImageField(default='100.jpeg', upload_to=None)),
                ('url_r', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
            ],
            options={
                'verbose_name': 'Маршруты',
                'verbose_name_plural': 'Маршруты',
                'db_table': 'routes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Сountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Наименование')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('url_c', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('routes', models.ManyToManyField(to='catalog.route')),
            ],
            options={
                'verbose_name': 'Страны',
                'verbose_name_plural': 'Страны',
                'db_table': 'countries',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('address', models.CharField(max_length=150)),
                ('working_hours', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('image', models.ImageField(default='100.jpeg', upload_to=None)),
                ('url_b', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.route', verbose_name='Маршрут')),
                ('country_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='catalog.сountry', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Пивоварни',
                'verbose_name_plural': 'Пивоварни',
                'db_table': 'breweries',
                'ordering': ['title'],
            },
        ),
    ]
