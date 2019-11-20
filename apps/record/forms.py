from django import forms
from .models import Record

#convencion de nombres de clases segun el nombre del modelo
class RecordForm(forms.ModelForm):
    #si heredas forms.ModelForm hereda la esructura visual y no necesitas especificar en html
    #si heredas form debes definir la estructura html del formulario
    class Meta:
        model = Record
        fields = ['sensor', 'value']