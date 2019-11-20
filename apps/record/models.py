from django.db import models
    

class Record(models.Model):
    id = models.AutoField(primary_key = True)
    create_at = models.DateField("Fecha de creación", auto_now = True, auto_now_add = False)
    sensor = models.FloatField(max_length = 200, blank = False, null = False)
    value = models.FloatField(max_length = 200, blank = False, null = False)
    #la fecha de creacion se auto agregara al cearlo y auto actualizara si se modifica
    #IntegerField
    #JsonField
    #URLField
    #ImageField
    #FileField
    #BolleanField

    #define el nombre en plurar y singular de la clase
    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'
        ordering = ['value'] #ordena por nombre los objetos

    #muestra el nombre del objeto creado
    def __str__(self):
        return self.value