from django import forms
from .models import Mensaje

class MensajeForm(forms.Form):
    contenido = forms.CharField(
        widget=forms.Textarea(attrs={'rows':4, 'placeholder': 'Escribe tu mensaje aquí...'}),
        label='Mensaje'
    )