from django.contrib import admin
from .models import Inventario,Inventario_Material

# Register your models here.


class InventarioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Inventario, InventarioAdmin)


class Inventario_materialAdmin(admin.ModelAdmin):
    pass
admin.site.register(Inventario_Material,Inventario_materialAdmin)
