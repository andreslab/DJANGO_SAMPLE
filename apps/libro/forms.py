from django import forms
from .models import Autor

#convencion de nombres de clases segun el nombre del modelo
class AutorForm(forms.ModelForm):
    #si heredas forms.ModelForm hereda la esructura visual y no necesitas especificar en html
    #si heredas form debes definir la estructura html del formulario
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad', 'descripcion']