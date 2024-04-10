# Generated by Django 5.0.2 on 2024-03-22 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_route_route_cities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='сountry',
            name='breweries',
        ),
        migrations.AddField(
            model_name='brewery',
            name='country_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.сountry', verbose_name='Страна'),
        ),
    ]
