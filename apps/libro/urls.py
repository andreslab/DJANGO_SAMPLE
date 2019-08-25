from django.urls import path, include
from .views import crearAutor, listarAutor

urlpatterns = [
   path('crear_autor/', crearAutor, name = 'crear_autor'),
   path('lista_autores/', listarAutor, name = 'listar_autores')
]
