from django.urls import path
from . import views

urlpatterns = [
    path('', views.truck_entries, name='truck_entries'),
]