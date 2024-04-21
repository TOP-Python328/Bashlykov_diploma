from django.db import models
from django.urls import reverse
import uuid

def uuid_url():
    return uuid.uuid4()
    
class Route(models.Model):
    class Meta:
        db_table = 'routes'
        verbose_name='Маршруты'
        verbose_name_plural='Маршруты'
        ordering = ['id']
    
    name = models.CharField(verbose_name='Название маршрута', max_length=50, unique=True, error_messages={'unique': 'такой маршрут уже существует'})
    slug = models.SlugField(max_length=50, verbose_name="URL")
    route_cities = models.CharField(max_length=150, verbose_name='Города маршрута')
    travel_time = models.CharField(max_length=50, verbose_name='Длительность маршрута' )
    base_city = models.CharField(max_length=50, verbose_name='Базовый город')
    bus = models.CharField(max_length=50, blank=True, verbose_name='Общественный транспорт')
    description= models.CharField(max_length=500, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to=None, default='100.jpeg')
    image_city = models.ImageField(upload_to=None, default='100.jpeg')
    url_r = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, verbose_name="UUID")
  
    # def url(self) -> str:
        # return (self.url_r)
        
    def get_absolute_url(self):
        return reverse('route', kwargs={'route_slug': self.slug})
        
    def __repr__(self):
        return f'<{self.name}>'
    
    def __str__(self):
        return f'{self.name}'


class Сountry (models.Model):
    class Meta:
        db_table = 'countries'
        verbose_name='Страны'
        verbose_name_plural='Страны'
        ordering = ['id']
    
    name = models.CharField(verbose_name='Наименование', max_length=50, unique=True)
    slug = models.SlugField(max_length=50, verbose_name="URL")
    routes = models.ManyToManyField(Route)
    url_c = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, verbose_name="UUID")
        
    def get_absolute_url(self):
        return reverse('country', kwargs={'country_slug': self.slug})
    
    def __repr__(self):
        return self.name
        
    def __str__(self):
        return f'{self.name}'

class Brewery(models.Model):
    class Meta:
        db_table = 'breweries'
        verbose_name='Пивоварни'
        verbose_name_plural='Пивоварни'
        ordering = ['title']
        
    title = models.CharField(verbose_name='Название', max_length=50)
    slug = models.SlugField(max_length=50, verbose_name="URL")
    address = models.CharField(max_length=150)
    working_hours = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True )
    description= models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to=None, default='100.jpeg')
    route_id = models.ForeignKey(Route, verbose_name='Маршрут', on_delete=models.PROTECT)
    country_id = models.ForeignKey(Сountry, verbose_name='Страна', on_delete=models.PROTECT, default=1)
    url_b = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, verbose_name="UUID")
    
    # def url(self) -> str:
        # return (self.title)
    
    def get_absolute_url(self):
        return reverse('brewery', kwargs={'brewery_slug': self.slug})
    
    def __repr__(self):
        return f'<Пивоварня: {self.title}>'
    
    def __str__(self):
        return f'Пивоварня: {self.title}'