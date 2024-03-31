from django.shortcuts import render
from catalog.models import Route, Brewery, Сountry
from transliterate import translit

routes_name = {
    translit(route.name, 'ru', reversed=True).lower(): route
    for route in Route.objects.all()
}

countries_name = {
    translit(country.name, 'ru', reversed=True).lower(): country
    for country in Сountry.objects.all()
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
        }
    )
    
def route(request, name: str):
    route = routes_name[name]
    return render(
        request,
        'route.html',
        {
            'route': route,
            'breweries' : route.brewery_set.all(),
        }
    ) 
    
def route_brewery(request, name: str, id: int):
    return render(
        request,
        'route_brewery.html',
        {
            'brewery': Brewery.objects.get(id=id),
        }
    )    
    
def countries(request):
    return render(
        request,
        'countries.html',
        {
            'countries': Сountry.objects.all(),
        }
    )
    
def country(request, name: str):
    country = countries_name[name]
    return render(
        request,
        'country.html',
        {
            'country': country,
            'routes' : country.routes.all(),
        }
    ) 
    
def country_route(request, name: str, id: int):
    route = Route.objects.get(id=id)
    return render(
        request,
        'route.html',
        {
            'route': route,
            'breweries' : route.brewery_set.all(),
        }
    )    
    
# def country_route_brewery(request, name: str, id: int):
    # route = Route.objects.get(id=id)
    # return render(
        # request,
        # 'route.html',
        # {
            # 'route': route,
            # 'breweries' : route.brewery_set.all(),
        # }
    # )    