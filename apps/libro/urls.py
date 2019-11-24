from django.urls import path, include
from .views import crearAutor, listarAutor, editarAutor

urlpatterns = [
   path('crear_autor/', crearAutor, name = 'crear_autor'),
   path('listar_autores/', listarAutor, name = 'listar_autores'),
   path('editar_autor/<int:id>', editarAutor, name = 'editar_autor')

   #pasar parametros
   #path('lista_autores/<slug:titulo>', listarAutor, name = 'listar_autores') 
   # #estoy pasando un string con slug

   #usar re_path para agregar expresiones regulares
   #re_path(r'^crear_autor/(?P<id>\d)', listarAutor, name = 'listar_autores' )
]
