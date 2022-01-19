from django.utils.datetime_safe import datetime
from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Gestion.models import Producto
from .forms import add2cartForm,clienteChoiceForm
from django.views.generic import ListView
from .carrito import Carrito,Comprador
from Personas.models import Cliente
from django.shortcuts import redirect, get_object_or_404
from django.http import FileResponse
from .models import Venta
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='next', login_url="/auth/login/")
def index1(request):
    form = clienteChoiceForm(request.POST)
    consulta = request.GET.get('nombre')
    if consulta:
        query = Producto.objects.filter(nombre__icontains=consulta)
    else:
        query = Producto.objects.all()
    if form.is_valid():
        iden = form.cleaned_data['comprador']
        comprador = Comprador(request)
        cliente = Cliente.objects.get(identificacion=iden.identificacion)
        comprador.add(cliente)
    context = {
    'query':query,
    'formCliente':form
    }
    return render(request,'Ventas/index.html',context)

class index(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    login_url = 'auth/login/'
    permission_required = 'Ventas.view_venta'
    template_name = "Ventas/index.html"
    model = Producto
    formCliente = clienteChoiceForm
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
        return redirect('/venta/')
        
    context={'object':object,'form':form}


    return render(request,'Ventas/update.html',context)

    #Carrito

def agregar_carrito(request,pk):
    producto = Producto.objects.get(id=pk)
    carrito=Carrito(request)
    carrito.add(producto)
    return redirect('/venta/')

def eliminar_producto(request,pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=pk)
    carrito.remove(producto)
    return redirect('/venta/')

def restar_producto(request,pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=pk)
    carrito.decrement(producto)
    return redirect('/venta/')

def limpiar(request):
    carrito = Carrito(request)
    carrito.clear()
    return redirect("/venta/")


#PAGO
def pagar(request):
    carrito = Carrito(request)
    response = HttpResponse(content_type='Application/pdf')
    d = datetime.today().strftime('%d-%m-%Y')
    response['Content-Disposition']=f'inline; filename="{d}.pdf"'
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    c_compra = request.session["carrito"]
    ide = []
    nombre = []
    cantidad = []
    valor = []
    p_unitario = []
    aux=0
    aux1 =0
    total =0
    test = request.session["comprador"]
    if test:
        for row in test.keys():
            q = Cliente.objects.get(identificacion = test[row]["comprador_id"]) 
            p.drawString(50,720,"A Nombre de: "+ str(q))
    else:
        p.drawString(50,720,"A Nombre de: Invitado")
    for row in c_compra.keys():
            ide.append(c_compra[row]["producto_id"])
            nombre.append(c_compra[row]["nombre"])
            aux1 =c_compra[row]["cantidad"]
            cantidad.append(str(aux1))
            aux = c_compra[row]["acmuluado"]
            valor.append(str(aux))
            p_unitario.append(str(c_compra[row]["unitario"]))
    p.setFont("Helvetica",15,leading=None)
    p.setFillColorRGB(0.29296875,0.453125,0.609375)
    p.drawString(260,800,"Papeleria Y Variedades Dangedav")
    p.line(0,780,1000,780)
    p.line(0,780,1000,778)
    p.drawString(200,750,"FACTURA DE COMPRA")
    #render
    p.setFont("Helvetica",10,leading=None)
    p.drawString(50,690,"Producto ") 
    x =670
    for elemento in nombre:
        p.drawString(50,x,elemento)
        x = x -10

    x =670
    p.drawString(250,690,"Precio Unitario ") 
    for elemento in p_unitario:
        p.drawString(250,x,elemento)
        x = x -10
    x =670
    p.drawString(350,690,"Cantidad") 
    for elemento in cantidad:
        p.drawString(350,x,elemento)
        x = x -10
    x =670
    p.drawString(450,690,"Subtotal") 
    for elemento in valor:
        p.drawString(450,x,elemento)
        x = x -10  
    for key, value in request.session["carrito"].items():
        total += int(value["acmuluado"])
    p.setFont("Helvetica",15,leading=None)
    p.drawString(50,50,"Total")
    p.drawString(400,50,"$") 
    p.drawString(415,50,str(total))
    p.setTitle(f'Report on {d}')
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    carrito.pay()
    comprador = Comprador(request)
    carrito = Carrito(request)
    carrito.clear()
    comprador.clear()
    return response

#cotizacion
def generar_pdf(request):
    username = request.user.username
    response = HttpResponse(content_type='Application/pdf')
    d = datetime.today().strftime('%d-%m-%Y')
    response['Content-Disposition']=f'inline; filename="{d}.pdf"'
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    c_compra = request.session["carrito"]
    ide = []
    nombre = []
    cantidad = []
    valor = []
    p_unitario = []
    aux=0
    aux1 =0
    total =0
    test = request.session["comprador"]
    if test:
        for row in test.keys():
            q = Cliente.objects.get(identificacion = test[row]["comprador_id"]) 
            p.drawString(50,720,"A Nombre de: "+ str(q))
    else:
        p.drawString(50,720,"A Nombre de: Invitado")
    for row in c_compra.keys():
            ide.append(c_compra[row]["producto_id"])
            nombre.append(c_compra[row]["nombre"])
            aux1 =c_compra[row]["cantidad"]
            cantidad.append(str(aux1))
            aux = c_compra[row]["acmuluado"]
            valor.append(str(aux))
            p_unitario.append(str(c_compra[row]["unitario"]))
    p.setFont("Helvetica",15,leading=None)
    p.setFillColorRGB(0.29296875,0.453125,0.609375)
    p.drawString(270,800,"Papeleria Y Variedades Dangedav")
    p.line(0,780,1000,780)
    p.line(0,780,1000,778)
    p.drawString(200,750,"FACTURA DE COMPRA")

    p.drawString(180,25,"Procesado por "+username + " el " + d) 

    #render
    p.setFont("Helvetica",10,leading=None)
    p.drawString(50,690,"Producto ") 
    x =670
    for elemento in nombre:
        p.drawString(50,x,elemento)
        x = x -10

    x =670
    p.drawString(250,690,"Precio Unitario ") 
    for elemento in p_unitario:
        p.drawString(250,x,elemento)
        x = x -10
    x =670
    p.drawString(350,690,"Cantidad") 
    for elemento in cantidad:
        p.drawString(350,x,elemento)
        x = x -10
    x =670
    p.drawString(450,690,"Subtotal") 
    for elemento in valor:
        p.drawString(450,x,elemento)
        x = x -10  
    for key, value in request.session["carrito"].items():
        total += int(value["acmuluado"])
    p.setFont("Helvetica",15,leading=None)
    p.drawString(50,50,"Total")
    p.drawString(400,50,"$") 
    p.drawString(415,50,str(total))
    p.setTitle(f'Report on {d}')
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    comprador = Comprador(request)
    carrito = Carrito(request)
    carrito.clear()
    comprador.clear()
    return response

class VentaListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    ogin_url = 'auth/login/'
    permission_required = 'Ventas.view_venta'
    model = Venta
    template_name = "Ventas/historico.html"

def clearComp(request):
    comprador = Comprador(request)
    comprador.clear()
    return redirect("/venta/")