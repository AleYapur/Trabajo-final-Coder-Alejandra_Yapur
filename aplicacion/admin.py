from django.contrib import admin

from .models import *

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "id")
    list_filter = ("nombre",)


class OrdenAdmin(admin.ModelAdmin):
    list_display = ("orden_id",)
    list_filter = ("orden_id",)
    
    
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Avatar)
admin.site.register(Orden, OrdenAdmin)