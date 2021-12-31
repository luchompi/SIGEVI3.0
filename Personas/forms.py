from django import forms


class clienteForm(forms.Form):
    identificacion=forms.CharField()
    nombre=forms.CharField()
    apellido=forms.CharField()
    direccion=forms.CharField()
    telefono=forms.CharField()
    correo=forms.EmailField()
    
class proveedorForm(forms.Form):
        NIT=forms.CharField()
        razonSocial=forms.CharField()
        direccionEmpresa=forms.CharField()
        direccionVenta=forms.CharField()
        telefono=forms.CharField()
        correo=forms.CharField()
