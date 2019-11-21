from django.urls import path, include
from .views import crearAutor, listarAutor

urlpatterns = [
   path('crear_autor/', crearAutor, name = 'crear_autor'),
   path('lista_autores/', listarAutor, name = 'listar_autores')

   #pasar parametros
   #path('lista_autores/<slug:titulo>', listarAutor, name = 'listar_autores') 
   # #estoy pasando un string con slug

   #usar re_path para agregar expresiones regulares
   #re_path(r'^crear_autor/(?P<id>\d)', listarAutor, name = 'listar_autores' )
]
