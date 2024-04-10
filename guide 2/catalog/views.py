from django.shortcuts import render
from transliterate import translit

from catalog.models import Route, Brewery, Сountry
from catalog.forms import (
    AddСountryForm, 
    
)
# routes_name = {
#     translit(route.name, 'ru', reversed=True).lower(): route
#     for route in Route.objects.all()
# }
# 
# countries_name = {
#     translit(country.name, 'ru', reversed=True).lower(): country
#     for country in Сountry.objects.all()
# }
# 
# breweries_name = {
#     translit(brewery.title, 'ru', reversed=True).lower(): brewery
#     for brewery in Brewery.objects.all()
# }

def main(request):
    return render(
        request,
        'main.html',
    )
    
def routes(request):
    return render(
        request,
        'routes.html',
        {
            'routes': Route.objects.all(),
        } )
    
def route(request, name: str):
    route = routes_name[name]
    return render(
        request,
        'route.html',
        {
            'route': route,
            'breweries' : route.brewery_set.all(),
        } ) 
    
def route_brewery(request, name: str, title: str):
    brewery = breweries_name[title] 
    return render(
        request,
        'route_brewery.html',
        {
            'brewery': brewery,
        } )    
    
def countries(request):
    return render(
        request,
        'countries.html',
        {
            'countries': Сountry.objects.all(),
        } )
    
def country(request, name: str):
    country = countries_name[name]
    return render(
        request,
        'country.html',
        {
            'country': country,
            'routes' : country.routes.all(),
        } ) 
    
def country_route(request, name: str, id: int):
    route = Route.objects.get(id=id)
    return render(
        request,
        'route.html',
        {
            'route': route,
            'breweries' : route.brewery_set.all(),
        } )    
     
def country_route_brewery(request, name: str, id: int, title: str):
    brewery = breweries_name[title] 
    return render(
        request,
        'route_brewery.html',
        {
            'brewery': brewery,
        } )    

def breweries(request):
    return render(
        request,
        'breweries.html',
        {
            'breweries': Brewery.objects.all(),
        } )
    
def brewery(request, title: str):
    brewery = breweries_name[title]
    return render(
        request,
        'route_brewery.html',
        {
            'brewery': brewery,
        } ) 
    
def add_brewery(request):
    context = {
        'added': False,
        'countries': Сountry.objects.all(),
        'routes': Route.objects.all(),
        'double': False,
    }
    if request.method == 'POST':
        title = request.POST['title']
        address = request.POST['address']
        working_hours = request.POST['working_hours']
        link = request.POST['link']
        description = request.POST['description']
        route_id = int(request.POST['route_id'])
        country_id = int(request.POST['country_id'])
        double = Brewery.objects.filter(title=title, link=link,country_id=country_id)
        if not double:
            Book(title=title, address=address, working_hours=working_hours, link=link, description=description, route_id=route_id, country_id=country_id).save()
            context['added'] = True
        else:
            context['double'] = True
        
    return render(
        request,
        'add_brewery.html',
        context
    )
    
def add_country(request):
    if request.method == 'GET':
        form = AddСountryForm()
    
    elif request.method == 'POST':
        form = AddСountryForm(request.POST)
        if form.is_valid():
            Сountry(**form.cleaned_data).save()
            form = AddСountryForm()
    
    return render(
        request,
        'add_country.html',
        {'form': form}
    )