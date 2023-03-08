from django.contrib import admin
from django.urls import path
from tours.views import *


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('departure/', DepartureView.as_view(), name='departure'),
    path('spb/', SpbView.as_view(), name='spb'),
    path('nsk/', NskView.as_view(), name='nsk'),
    path('ekb/', EkbView.as_view(), name='ekb'),
    path('kazan/', KazanView.as_view(), name='kazan'),
    path('tour/', TourView.as_view(), name='tour'),

]
