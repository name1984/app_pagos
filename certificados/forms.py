#encoding:utf-8

from django import forms
from django.forms import ModelForm
import models
from models import Usuario, Direccion, Provincia, Ciudad, Transaccion

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario

class DireccionForm(ModelForm):
    #cod_city = forms.ModelChoiceField(queryset=models.Ciudad.objects.none())

    class Meta:
        model = Direccion
     #   fields = ['principal', 'secundaria', 'referencia', 'cod_usuario','cod_prov']
     #   exclude = ['cod_city']

class ProvinciaForm(ModelForm):
    class Meta:
        model = Provincia

class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad

class TransaccionForm(ModelForm):
    class Meta:
        model = Transaccion

class BuscarUsuarioForm(models.Form):
    usuario = forms.CharField(label='Participante')
