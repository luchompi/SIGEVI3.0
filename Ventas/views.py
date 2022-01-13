from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Gestion.models import Producto
from .forms import add2cartForm
from django.views.generic import ListView
from .carrito import Carrito
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

class index(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    login_url = 'auth/login/'
    permission_required = 'Ventas.view_venta'
    template_name = "Ventas/index.html"
    model = Producto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consulta=self.request.GET.get('nombre')
        if consulta:
            context["query"] = Producto.objects.filter(nombre__icontains=consulta)
        else:
            context["query"] = Producto.objects.all()
        return context


def ProductoList(request,pk):
    
    object = Producto.objects.get(pk=pk)
    form = add2cartForm(request.POST)
  
    if form.is_valid():
        cantidad = form.cleaned_data['quantity']
        carrito = Carrito(request)
        carrito.add(object,cantidad)
    else:
        print("form no valido")
    context={'object':object,'form':form}


    return render(request,'Ventas/update.html',context)

    #Carrito

def agregar_carrito(request,pk):
    print("consulta")
    producto = Producto.objects.get(id=pk)
    print("cantidad")
    print("Carrito")
    carrito=Carrito(request)
    print("añadir")
    carrito.add(producto)
    return redirect('/venta/')

def eliminar_producto(request,pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=pk)
    carrito.remove(producto)
    return redirect("venta:productoIndex")

def restar_producto(request,pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=pk)
    carrito.decrement(producto)
    return redirect('/venta/')

def limpiar(request):
    carrito = Carrito(request)
    carrito.clear()
    return redirect("/venta/")

def pagar(request):
    carrito = Carrito(request)
    carrito.pay()
