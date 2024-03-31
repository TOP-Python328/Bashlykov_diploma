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
    path('route/<str:name>/<int:id>/', views.route_brewery, name='route_brewery'),
    path('countries', views.countries, name='countries'),
    path('country/<str:name>/', views.country, name='country'),
    path('country/<str:name>/<int:id>/', views.country_route, name='country_route'),
    
    
    # path('detail_routes', views.detail_routes, name='detail_routes'),
    # path('route_cities', views.route_cities, name='route_cities'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
