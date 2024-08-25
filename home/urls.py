from django.urls import path
from . import views
#Esse vai tratar a rota do django.


urlpatterns = [
    path('', views.index, name='index'),
]
