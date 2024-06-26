"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls ),
    path('', views.main, name='main'),
    path('routes', views.routes, name='routes'),
    path('route/<slug:route_slug>/', views.route, name='route'),
    path('route/<slug:route_slug>/brewery/', views.route_breweries, name='route_breweries'),
    path('route/<slug:route_slug>/brewery/<slug:brewery_slug>/', views.route_brewery, name='route_brewery'),
    path('route/<slug:route_slug>/base_city/', views.route_city, name='route_city'),
    path('route/<slug:route_slug>/bus/', views.route_bus, name='route_bus'),
    path('route/<slug:route_slug>/description/', views.route_description, name='route_description'),
    
    path('countries', views.countries, name='countries'),
    path('country/<slug:country_slug>/', views.country, name='country'),
    path('country/<slug:country_slug>/<slug:route_slug>/', views.country_route, name='country_route'),
    path('country/<slug:country_slug>/<slug:route_slug>/brewery/', views.country_route_breweries, name='country_route_breweries'),
    path('country/<slug:country_slug>/<slug:route_slug>/brewery/<slug:brewery_slug>/', views.country_route_brewery, name='country_route_brewery'),
    
    path('breweries', views.breweries, name='breweries'),
    path('brewery/<slug:brewery_slug>/', views.brewery, name='brewery'),
    
    path('add_route', views.add_route, name='add_route'),
    path('add_country', views.add_country, name='add_country'),
    path('add_brewery', views.add_brewery, name='add_brewery'),
    
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    
    path('register', views.register, name='user_register'),
    path('login', views.login, name='user_login'),
    path('logout', views.logout, name='user_logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
