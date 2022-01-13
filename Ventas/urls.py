from django.urls import path
from . import views as v

app_name = 'ventas'

urlpatterns=[
path('',v.index.as_view(),name='ventaIndex'),
path('detalles/<pk>/',v.ProductoList,name="VentaProductoDetalle"),



	#Carrito
    path('agregar/<pk>/',v.agregar_carrito,name="add"),
    path('eliminar/<pk>/',v.eliminar_producto,name="del"),
    path('restar/<pk>/',v.restar_producto,name="remove"),
    path('limpiar/',v.limpiar,name="cls"),
    path('pay/',v.pagar,name="pay"),


]
