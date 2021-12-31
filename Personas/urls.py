from django.urls import path
from . import views as v

app_name = "personas"

urlpatterns = [
    #urls Clientes
    path('clientes/',v.ClienteCreateView.as_view(),name="clienteIndex"),
    path('clientes/actualizar/<pk>/',v.ClienteUpdateView.as_view(),name="clienteUpdate"),
    path('cliente/eliminar/<pk>/',v.ClienteDeleteView.as_view(),name="clienteDelete"),

    #urls Proveedores
    path('proveedores/',v.ProveedorCreateView.as_view(),name="proveedorIndex"),
    path('proveedores/actualizar/<pk>/',v.ProveedorUpdateView.as_view(),name="proveedorUpdate"),
    path('proveedores/eliminar/<pk>/',v.ProveedorDeleteView.as_view(),name="proveedorDelete"),


]
