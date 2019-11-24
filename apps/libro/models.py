from django.db import models
    

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellido = models.CharField(max_length = 200, blank = False, null = False)
    nacionalidad = models.CharField(max_length = 200, blank = False, null = False)
    descripcion = models.TextField(blank = False, null = False)
    fecha_creacion = models.DateField("Fecha de creación", auto_now = True, auto_now_add = False)
    estado = models.BooleanField('Estado', default = True)
    #la fecha de creacion se auto agregara al cearlo y auto actualizara si se modifica
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


class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField("Título", max_length = 255, blank = False, null = False)
    fecha_publicacion = models.DateField("Fecha de publicación", blank = False, null = False)
    fecha_creacion = models.DateField("Fecha de creación", auto_now = True, auto_now_add = False)
    
    #autor_id = models.OneToOneField(Autor, on_delete = models.CASCADE)
    
    #on_delete indica que se eliminara la relacion al eliminar el objeto
    #oneToOneField : indica la relacion de uno a uno en una base de datos, un libro solo puede tener un autor y un autor solo un libro
    #para este caso si un libro ya es asignado a un autor, creando otro libro necsitaria otro autor
    #para una relaciones de uno a muchos se usa una clave foranea "ForeignKey"
    
    #autor_id = models.ForeignKey(Autor, on_delete = models.CASCADE)

    #para una relacion de muchos a muchos se usa:
    autor_id = models.ManyToManyField(Autor)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str___(self):
        return self.titulo