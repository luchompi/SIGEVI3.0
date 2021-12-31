from django.db import models
from django.db.models.deletion import SET_NULL
from Personas.models import Proveedor
# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50,verbose_name="Digite nombre de Categoría",unique=True, error_messages={'unique':'ya existe esta categoria'})
    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre= models.CharField(max_length=50,verbose_name="Digite nombre de la Marca",unique=True,error_messages={'unique':'Ya existe esta marca en el sistema'})
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    class unidades(models.TextChoices):
        unidad = "Unidad"
        docena = "Docena"
        resma = "Resma"
        caja = "Caja"
    
    categoria=models.ForeignKey(Categoria,to_field='id',on_delete=SET_NULL,null=True,blank=True,verbose_name="Seleccione Categoría del producto")
    nombre=models.CharField(max_length=50,verbose_name="Ingrese nombre del producto")
    cantidad=models.IntegerField(verbose_name="Indique Cantidad de Producto")
    unidad = models.CharField(max_length=12,choices=unidades.choices,default="Unidad")
    precio_compra = models.IntegerField(verbose_name="Indique el Valor del producto")
    proveedor=models.ForeignKey(Proveedor,on_delete=SET_NULL,null=True,blank=True,verbose_name="Indique Proveedor")
    marca=models.ForeignKey(Marca,on_delete=SET_NULL,null=True,blank=True,verbose_name="Especifique la marca del producto")
    def __str__(self):
        return self.nombre

