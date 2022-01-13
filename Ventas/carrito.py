
from Gestion.models import Producto


class Carrito:
    def __init__(self,request):
        self.resquest = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
            
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