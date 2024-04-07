from django.db import models
from transliterate import translit

from functools import cached_property
import random
from random import randint

class Route(models.Model):
    class Meta:
        db_table = 'routes'
    
    name = models.CharField(verbose_name='Название маршрута', max_length=50)
    route_cities = models.CharField(max_length=150, verbose_name='Города маршрута')
    travel_time = models.CharField(max_length=50)
    base_city = models.CharField(max_length=50)
    bus = models.CharField(max_length=50, blank=True)
    description= models.CharField(max_length=500, blank=True)
  
    @cached_property
    def url(self) -> str:
        return translit(self.name, 'ru', reversed=True).lower()
    
    def url_1(self) -> str:
        return (self.id)
        
    def __repr__(self):
        return f'<{self.name}>'
    
    def __str__(self):
        return f'{self.name}'


class Сountry (models.Model):
    class Meta:
        db_table = 'countries'
    
    name = models.CharField(verbose_name='Наименование', max_length=50)
    routes = models.ManyToManyField(Route)
    
    @cached_property
    def url(self) -> str:
        return translit(self.name, 'ru', reversed=True).lower()
        
    def __repr__(self):
        return self.name
        
    def __str__(self):
        return f'{self.name}'

class Brewery(models.Model):
    class Meta:
        db_table = 'breweries'
        
    title = models.CharField(verbose_name='Название', max_length=50)
    address = models.CharField(max_length=150)
    working_hours = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True )
    description= models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to=None, default='100.jpeg')
    route_id = models.ForeignKey(Route, verbose_name='Маршрут', on_delete=models.CASCADE)
    country_id = models.ForeignKey(Сountry, verbose_name='Страна', on_delete=models.CASCADE, default=1)

    @cached_property
    def url(self) -> str:
        return translit(self.title, 'ru', reversed=True).lower()
    
    # def url(self) -> str:
        # return (self.title)
    
    def __repr__(self):
        return f'<Пивоварня: {self.title}>'
    
    def __str__(self):
        return f'Пивоварня: {self.title}'


# def uuid_url():
    # return uuid.getnode()
    # или
    # return int(random.random() * 100)
     
# class Route(models.Model):
    
    # class Meta:
        # db_table = 'routes'
        # 1 вариант
    # url_r = models.CharField(max_length=100, default=uuid_url(), editable=False)
        # 2 вариант
    # url_r = models.UUIDField(default=uuid.getnode, unique= True, editable=False)