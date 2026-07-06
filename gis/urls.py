from django.urls import path
from . import views

urlpatterns = [
    path('', views.gis_dashboard, name='gis_dashboard'),
]