from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Marca,Categoria,Producto
from .forms import productoForm,marcaForm,categoriaForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#Operaciones de Marcas
class MarcaCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = 'auth/login/'
    permission_required = 'Gestion.add_marca'
    model = Marca
    form = marcaForm
    fields =[
        'nombre',
    ]
    template_name = "Marca/index.html"
    success_url = '.'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('nombre'):
            context["query"] = Marca.objects.filter(nombre__icontains=consulta)
        else:
            context["query"] = Marca.objects.all()
        return context

class MarcaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='/auth/login'
    permission_required=['Gestion.view_marca','Gestion.change_marca']
    model = Marca
    form = marcaForm
    fields =[
        'nombre',
    ]
    success_url = "/gestion/marca/actualizar/{id}"
    template_name = "Marca/update.html"

class MarcaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url='/auth/login'
    permission_required='Gestion.delete_marca'
    model = Marca
    template_name = "Marca/delete.html"
    success_url = "/gestion/marca/"

#Operaciones de Categoría
class CategoriaCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = 'auth/login/'
    permission_required = 'Gestion.add_marca'
    model = Categoria
    form = categoriaForm
    fields =[
        'nombre',
    ]
    template_name = "Categoria/index.html"
    success_url = '.'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('marca'):
            context["query"] = Categoria.objects.filter(nombre__icontains=consulta)
            print(context)
        else:
            context["query"] = Categoria.objects.all()
        return context

class CategoriaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='/auth/login'
    permission_required=['Gestion.view_marca','Gestion.change_marca']
    model = Categoria
    form = categoriaForm
    fields =[
        'nombre',
    ]
    success_url = "/gestion/categoria/actualizar/{id}"
    template_name = "Categoria/update.html"

class CategoriaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url='/auth/login'
    permission_required='Gestion.delete_categoria'
    model = Categoria
    template_name = "Categoria/delete.html"
    success_url = "/gestion/categoria/"

#Operaciones de Productos
class ProductoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = 'auth/login/'
    permission_required = 'Gestion.add_producto'
    model = Producto
    form = productoForm
    fields =[
        'categoria',
        'nombre',
        'cantidad',
        'unidad',
        'precio_compra',
        'proveedor',
        'marca',
    ]
    template_name = "Producto/index.html"
    success_url = '.'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('nombre'):
            context["query"] = Producto.objects.filter(nombre__icontains=consulta)
        else:
            context["query"] = Producto.objects.all()
        return context

class ProductoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='/auth/login'
    permission_required=['Gestion.view_producto','Gestion.change_producto']
    model = Producto
    form = productoForm
    fields =[
        'categoria',
        'nombre',
        'cantidad',
        'unidad',
        'precio_compra',
        'proveedor',
        'marca',
    ]
    success_url = "/gestion/producto/actualizar/{id}"
    template_name = "Producto/update.html"


class ProductoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url='/auth/login'
    permission_required='Gestion.delete_producto'
    model = Producto
    template_name = "Producto/delete.html"
    success_url = "/gestion/producto/"
