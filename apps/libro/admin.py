from django.contrib import admin
from .models import Autor, Libro

#registrar modelos creados

admin.site.register(Autor)
admin.site.register(Libro)