from django.contrib import admin
from django.urls import path
from tours.views import MainView, DepartureView, TourView


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('departure/', DepartureView.as_view(), name='departure'),
    path('tour/', TourView.as_view(), name='tour'),

]
