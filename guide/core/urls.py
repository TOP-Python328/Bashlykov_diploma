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
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('routes', views.routes, name='routes'),
    path('route/<str:name>/', views.route, name='route'),
    path('route/<str:name>/brewery/', views.route_breweries, name='route_breweries'),
    path('route/<str:name>/brewery/<str:title>/', views.route_brewery, name='route_brewery'),
    
    path('countries', views.countries, name='countries'),
    path('country/<str:name>/', views.country, name='country'),
    path('country/<str:name>/<int:id>/', views.country_route, name='country_route'),
    path('country/<str:name>/<int:id>/brewery/', views.country_route_breweries, name='country_route_breweries'),
    path('country/<str:name>/<int:id>/brewery/<str:title>/', views.country_route_brewery, name='country_route_brewery'),
    
    path('breweries', views.breweries, name='breweries'),
    path('brewery/<str:title>/', views.brewery, name='brewery'),
    
    path('add_route', views.add_route, name='add_route'),
    path('add_country', views.add_country, name='add_country'),
    path('add_brewery', views.add_brewery, name='add_brewery'),
    
    path('register', views.register, name='user_register'),
    path('login', views.login, name='user_login'),
    path('logout', views.logout, name='user_logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
