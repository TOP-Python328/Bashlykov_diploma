# Generated by Django 5.0.2 on 2024-04-20 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='image_city',
            field=models.ImageField(default='100.jpeg', upload_to=None),
        ),
    ]