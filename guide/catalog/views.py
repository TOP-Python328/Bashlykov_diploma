from django.shortcuts import render, redirect
from transliterate import translit

from catalog.models import Route, Brewery, Сountry
from catalog.forms import (
    AddСountryForm, 
    AddRouteForm,  
)
from django.contrib.auth import (
    authenticate, 
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

routes_name = {
    translit(route.name, 'ru', reversed=True).lower(): route
    for route in Route.objects.all()
}

countries_name = {
    translit(country.name, 'ru', reversed=True).lower(): country
    for country in Сountry.objects.all()
}

breweries_name = {
    translit(brewery.title, 'ru', reversed=True).lower(): brewery
    for brewery in Brewery.objects.all()
}

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
        } ) 
        
def route_breweries(request, name: str):
    route = routes_name[name]
    return render(
        request,
        'route_breweries.html',
        {
            'route': route,
            'breweries' : route.brewery_set.all(),
        } ) 
    
def route_brewery(request, name: str, title: str):
    brewery = breweries_name[title]
    route = routes_name[name]
    return render(
        request,
        'route_brewery.html',
        {
            'route': route,
            'brewery': brewery,
            'breweries' : route.brewery_set.all(),
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
        
def country_route_breweries(request, name: str, id: int):
    route = Route.objects.get(id=id)
    return render(
        request,
        'route_breweries.html',
        {
            'route': route,
            'breweries' : route.brewery_set.all(),
        } )      
     
def country_route_brewery(request, name: str, id: int, title: str):
    brewery = breweries_name[title] 
    country = countries_name[name]
    route = Route.objects.get(id=id)
    return render(
        request,
        'route_brewery.html',
        {
            'route': route,
            'brewery': brewery,
            'breweries' : route.brewery_set.all(),
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
    
def add_route(request):
    if request.method == 'GET':
        form = AddRouteForm()
    
    elif request.method == 'POST':
        form = AddRouteForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddRouteForm()
    
    return render(
        request,
        'add_route.html',
        {
            'form': form,
        }
    )
    
def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
    
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main', permanent=True)
    
    return render(
        request,
        'register.html',
        {'form': form}
    )
    
def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
    
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('main', permanent=True)
        
    return render(
        request,
        'login.html',
        {'form': form}
    )
    
def logout(request):
    auth_logout(request)
    return redirect('main', permanent=True)