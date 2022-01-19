from django.urls import path
from . import views as v

app_name = 'ventas'

urlpatterns=[
path('',v.index1,name='ventaIndex'),
path('historico/',v.VentaListView.as_view(),name='ventaHistorico'),
path('detalles/<pk>/',v.ProductoList,name="VentaProductoDetalle"),



	#Carrito
    path('agregar/<pk>/',v.agregar_carrito,name="add"),
    path('eliminar/<pk>/',v.eliminar_producto,name="del"),
    path('restar/<pk>/',v.restar_producto,name="remove"),
    path('limpiar/',v.limpiar,name="cls"),
    path('pay/',v.pagar,name="pay"),
    path('PDF/',v.generar_pdf,name="PDF"),

    #comprador
    path('eliminar/',v.clearComp,name="delComp"),


]
