from django.urls import path, include
from .views import crearAutor

urlpatterns = [
   path('crear_autor/', crearAutor, name = 'crear_autor')
]
