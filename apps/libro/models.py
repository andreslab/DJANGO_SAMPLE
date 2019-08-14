from django.db import models
    

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellido = models.CharField(max_length = 200, blank = False, null = False)
    nacionalidad = models.CharField(max_length = 200, blank = False, null = False)
    descripcion = models.TextField(blank = False, null = False)
    #IntegerField
    #JsonField
    #URLField
    #ImageField
    #FileField
    #BolleanField

    #define el nombre en plurar y singular de la clase
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre'] #ordena por nombre los objetos

    #muestra el nombre del objeto creado
    def __str__(self):
        return self.nombre
