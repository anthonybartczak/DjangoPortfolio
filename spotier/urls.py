from django.urls import path
from . import views

urlpatterns = [
    path('spotier', views.index, name='index'),
]