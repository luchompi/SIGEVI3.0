
from Gestion.models import Producto
from Personas.models import Cliente

class Carrito:
    def __init__(self,request):
        self.resquest = request
        self.session = request.session
        if carrito := self.session.get("carrito"):
            self.carrito = carrito
        else:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
            
    def add(self,producto,cantidad):
        id = str(producto.pk)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.pk,
                "nombre":producto.nombre,
                "precio": producto.precio_compra,
                "cantidad":cantidad,
                "acmuluado":producto.precio_compra*cantidad,
                "unitario":producto.precio_compra,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acmuluado"] += producto.precio_compra
        self.save()
    
    def save(self):     
        self.session["carrito"]=self.carrito
        self.session.modified = True
    
    def remove(self,producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.save()
    
    def decrement(self,producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -=1  
            self.carrito[id]["acmuluado"] -=producto.precio_compra
            if self.carrito[id]["cantidad"] <=0: self.remove(producto)
            self.save()
            
    def clear(self):
        self.session["carrito"] = {}
        self.session.modified = True
#pagos
    def pay(self):
        for row in self.carrito.keys():
            ide = self.carrito[row]["producto_id"]
            object = Producto.objects.get(pk=ide)
            object.cantidad -= self.carrito[row]["cantidad"]
            object.save()
            
        self.session["carrito"] = {}
        self.session.modified = True

class Comprador:
    def __init__(self,request):
        self.request =  request
        self.session = request.session
        if comprador := self.session.get("comprador"):
            self.comprador = comprador
        else:
            self.session["comprador"] = {}
            self.comprador = self.session["comprador"]
    def add(self,cliente):
        id = str(cliente.pk)
        if id not in self.comprador.keys():
            self.comprador[id]={
                "comprador_id": cliente.pk,
                "nombre":cliente.nombre,
                "apellido":cliente.apellido,
                "telefono": cliente.telefono,
            }
        self.save()
    def save(self):     
        self.session["comprador"]=self.comprador
        self.session.modified = True
    def clear(self):
        self.session["comprador"] = {}
        self.session.modified = True