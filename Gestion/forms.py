from django import forms
from Personas.models import Proveedor
from .models import Marca,Categoria

class marcaForm(forms.Form):
    nombre=forms.CharField()

class categoriaForm(forms.Form):
    nombre = forms.CharField()


UNIDADES=[
    ('unidad' , "Unidad"),
    ('docena' , "Docena"),
    ('resma' , "Resma"),
    ( 'caja' , "Caja"),
]

class productoForm(forms.Form):
    categoria=forms.ModelChoiceField(queryset=Categoria.objects.all())
    nombre=forms.CharField()
    cantidad=forms.IntegerField()
    unidad = forms.Select(choices=UNIDADES)
    precio_compra = forms.IntegerField()
    proveedor=forms.ModelChoiceField(queryset=Proveedor.objects.all())
    marca=forms.ModelChoiceField(queryset=Marca.objects.all())
