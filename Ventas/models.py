from django.db import models
from django.db.models.deletion import SET_NULL
from Gestion.models import Producto
from Personas.models import Cliente

# Create your models here.


class Venta(models.Model):
    venta = models.FileField(upload_to='facturas',null=True,blank=True)
    comprador = models.ForeignKey(Cliente,on_delete=SET_NULL,null=True,blank=True)
    vendedor = models.CharField(max_length=50,null=True,blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
