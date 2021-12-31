from django.urls import path
from . import views as v

app_name="gestion"
urlpatterns = [
    #URL Marcas
    path('marca/',v.MarcaCreateView.as_view(),name="marcaIndex"),
    path('marca/actualizar/<pk>',v.MarcaUpdateView.as_view(),name="marcaUpdate"),
    path('marca/eliminar/<pk>',v.MarcaDeleteView.as_view(),name="marcaDelete"),
    
    #URL Categoria
    path('categoria/',v.CategoriaCreateView.as_view(),name="categoriaIndex"),
    path('categoria/actualizar/<pk>',v.CategoriaUpdateView.as_view(),name="categoriaUpdate"),
    path('categoria/eliminar/<pk>',v.CategoriaDeleteView.as_view(),name="categoriaDelete"),

    #URL Productos
    path('producto/',v.ProductoCreateView.as_view(),name="productoIndex"),
    path('producto/actualizar/<pk>',v.ProductoUpdateView.as_view(),name="productoUpdate"),
    path('producto/eliminar/<pk>',v.ProductoDeleteView.as_view(),name="productoDelete"),



]
