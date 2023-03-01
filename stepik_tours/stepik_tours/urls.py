"""stepik_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tours.views import *



urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('tour/', TourView.as_view(), name='tour'),
    path('hotel/', HotelView.as_view(), name='hotel'),
    path('admin/', admin.site.urls),
    path('departure/', DepartureView.as_view(), name='departure'),
    path('spb/', SpbView.as_view(), name='spb'),
    path('nsk/', NskView.as_view(), name='nsk'),
    path('ekb/', EkbView.as_view(), name='ekb'),
    path('kazan/', KazanView.as_view(), name='kazan'),
    path('card/', CardView.as_view(), name='card'),

]
