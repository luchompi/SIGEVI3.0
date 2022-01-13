#
from rest_framework import serializers
#
from Gestion.models import Producto
from .models import Venta

class productoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Producto
    fields = ('__all__')

class ordenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ('__all__')
