from django.urls import path
from . import views


urlpatterns = [
    path('', views.trip_form, name='trip_form'),
]