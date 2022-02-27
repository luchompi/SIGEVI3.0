from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Cliente,Proveedor
from .forms import clienteForm,proveedorForm

# Operaciones de Clientes
class ClienteCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = 'auth/login/'
    permission_required = ['Personas.add_cliente','Personas.view_cliente']
    model = Cliente
    form = clienteForm
    fields =[
        'identificacion',
        'nombre',
        'apellido',
        'direccion',
        'telefono',
        'correo',
    ]
    template_name = "Personas/index.html"
    success_url = '.'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('identificacion'):
            context["query"] = Cliente.objects.filter(identificacion__icontains=consulta)
        else:
            context["query"] = Cliente.objects.all()
        return context

class ClienteUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='/auth/login'
    permission_required=['Personas.view_cliente','Personas.change_cliente']
    model = Cliente
    form = clienteForm
    fields =[
        'identificacion',
        'nombre',
        'apellido',
        'direccion',
        'telefono',
        'correo',
    ]
    success_url = "/personas/clientes/actualizar/{identificacion}"
    template_name = "Personas/update.html"

class ClienteDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url='/auth/login'
    permission_required='Personas.delete_cliente'
    model = Cliente
    template_name = "Personas/delete.html"
    success_url = "/personas/clientes/"

#Operaciones de Proveedores
class ProveedorCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url='/auth/login'
    permission_required='Personas.add_proveedor','Personas.view_proveedor'
    model = Proveedor
    template_name = "Proveedor/index.html"
    form = proveedorForm
    fields =[
        'NIT',
        'razonSocial',
        'direccionEmpresa',
        'direccionVenta',
        'telefono',
        'correo',
    ]
    success_url = "."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('NIT'):
            context["query"] = Proveedor.objects.filter(NIT__icontains=consulta)
        else:
            context["query"] = Proveedor.objects.all()
        return context

class ProveedorUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='/auth/login'
    permission_required=['Personas.view_proveedor','Personas.change_proveedor']
    model = Proveedor
    form = proveedorForm
    fields =[
        'NIT',
        'razonSocial',
        'direccionEmpresa',
        'direccionVenta',
        'telefono',
        'correo',
    ]
    success_url = "/personas/proveedores/actualizar/{NIT}"
    template_name = "Proveedor/detail.html"

class ProveedorDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url='/auth/login'
    permission_required='Personas.delete_proveedor'
    model = Proveedor
    template_name = "Proveedor/delete.html"
    success_url = "/personas/proveedores/"