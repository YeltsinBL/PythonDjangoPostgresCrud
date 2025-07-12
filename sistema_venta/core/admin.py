from django.contrib import admin

# Register your models here.
from .models import Cliente, Categoria, Producto, Orden, DetalleOrden, Perfil, Proveedor

admin.site.register([Cliente, Categoria, Producto, Orden, DetalleOrden, Perfil, Proveedor])
