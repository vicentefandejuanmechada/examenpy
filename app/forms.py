from django import forms
from app.models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "Rut","Nombre","Apellido","Sector","Estado"