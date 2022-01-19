from Personas.models import Cliente
from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 200)]
class add2cartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)

class clienteChoiceForm(forms.Form):
    comprador = forms.ModelChoiceField(queryset=Cliente.objects.all())