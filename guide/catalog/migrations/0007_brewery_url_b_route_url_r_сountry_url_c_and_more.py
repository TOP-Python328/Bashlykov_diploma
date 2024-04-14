# Generated by Django 5.0.2 on 2024-04-14 12:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_brewery_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='url_b',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='route',
            name='url_r',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='сountry',
            name='url_c',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='image',
            field=models.ImageField(default='100.jpeg', upload_to=None),
        ),
        migrations.AlterField(
            model_name='route',
            name='base_city',
            field=models.CharField(max_length=50, verbose_name='Базовый город'),
        ),
        migrations.AlterField(
            model_name='route',
            name='bus',
            field=models.CharField(blank=True, max_length=50, verbose_name='Общественный транспорт'),
        ),
        migrations.AlterField(
            model_name='route',
            name='description',
            field=models.CharField(blank=True, max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(error_messages={'unique': 'такой маршрут уже существует'}, max_length=50, unique=True, verbose_name='Название маршрута'),
        ),
        migrations.AlterField(
            model_name='route',
            name='travel_time',
            field=models.CharField(max_length=50, verbose_name='Длительность маршрута'),
        ),
    ]
