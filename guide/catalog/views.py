from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.models import Route, Brewery, Сountry
from catalog.forms import (
    AddСountryForm, 
    AddRouteForm,
    RegisterUserForm    
)
from django.contrib.auth import (
    authenticate, 
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 

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
    
def route(request, route_slug):
    route = get_object_or_404(Route, slug=route_slug)
    return render(
        request,
        'route.html',
        {
            'route': route,
        } ) 

def route_city(request, route_slug):
    route = get_object_or_404(Route, slug=route_slug)
    return render(
        request,
        'route_city.html',
        {
            'route': route,
        } )

def route_bus(request, route_slug):
    route = get_object_or_404(Route, slug=route_slug)
    return render(
        request,
        'route_bus.html',
        {
            'route': route,
        } )

def route_description(request, route_slug):
    route = get_object_or_404(Route, slug=route_slug)
    return render(
        request,
        'route_description.html',
        {
            'route': route,
        } )                 
        
def route_breweries(request, route_slug):
    route = get_object_or_404(Route, slug=route_slug)
    return render(
        request,
        'route_breweries.html',
        {
            'route': route,
            'breweries' : route.brewery_set.all(),
        } ) 
  
def route_brewery(request, route_slug, brewery_slug):
    route = get_object_or_404(Route, slug=route_slug)
    brewery = get_object_or_404(Brewery, slug=brewery_slug) 
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
  
def country(request, country_slug):
    country = get_object_or_404(Сountry, slug=country_slug)
    return render(
        request,
        'country.html',
        {
            'country': country,
            'routes' : country.routes.all(),
        } ) 
    
def country_route(request, country_slug, route_slug):
    route = get_object_or_404(Route, slug=route_slug)
    return render(
        request,
        'route.html',
        {
            'route': route,
            'breweries' : route.brewery_set.all(),
        } )
        
def country_route_breweries(request, country_slug, route_slug):
    route = get_object_or_404(Route, slug=route_slug)
    return render(
        request,
        'route_breweries.html',
        {
            'route': route,
            'breweries' : route.brewery_set.all(),
        } )      
 
def country_route_brewery(request, country_slug, route_slug, brewery_slug):
    route = get_object_or_404(Route, slug=route_slug)
    country = get_object_or_404(Сountry, slug=country_slug)
    brewery = get_object_or_404(Brewery, slug=brewery_slug)
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
 
def brewery(request, brewery_slug):
    brewery = get_object_or_404(Brewery, slug=brewery_slug)  
    return render(
        request,
        'route_brewery.html',
        {
            'brewery': brewery,
        } ) 
        
@permission_required(perm='catalog.add_catalog', raise_exception=True)
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
        form = RegisterUserForm()
    
    elif request.method == 'POST':
        form = RegisterUserForm(request.POST)
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