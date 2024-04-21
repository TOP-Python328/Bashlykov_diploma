from django.contrib import admin

from catalog.models import *

class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'route_cities', 'travel_time', 'base_city', 'bus', 'description', 'image', 'url_r')
    list_display_links = ('id',)
    search_fields = ('name', 'description')
    list_editable = ('name', 'route_cities', 'travel_time', 'base_city', 'bus', 'image','description')
    list_filter = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class СountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'url_c')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_editable = ('name', 'slug')
    list_filter = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class BreweryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'address', 'working_hours', 'link', 'description','image', 'url_b', 'route_id', 'country_id')
    list_display_links = ('id',)
    search_fields = ('title', 'description')
    list_editable = ('title', 'slug', 'address', 'working_hours', 'link', 'description', 'image', 'route_id', 'country_id')
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Route, RouteAdmin)
admin.site.register(Сountry, СountryAdmin)
admin.site.register(Brewery, BreweryAdmin)

