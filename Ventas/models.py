from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import ManyToManyField
from Gestion.models import Producto
from Personas.models import Cliente
# Create your models here.
class Venta(models.Model):
    producto = models.ManyToManyField(Producto,to_field='id')
    comprador = models.ForeignKey(Cliente,on_delete=SET_NULL)
    vendedor = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['+datetime']