from django import forms
from .models import Marca, Modelo, Autoparte

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['nombre', 'marca']

class AutoparteForm(forms.ModelForm):
    class Meta:
        model = Autoparte
        fields = ['numero_serie', 'descripcion', 'marca', 'modelo']

class BuscarAutoparteForm(forms.Form):
    criterio = forms.CharField(
        label='Buscar por marca, modelo, descripción o nro de serie',
        max_length=100,
        required=False
    )