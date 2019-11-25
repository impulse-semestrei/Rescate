from django.contrib import admin
from .models import Inventario, InventarioMaterial

# Register your models here.


class InventarioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Inventario, InventarioAdmin)


class InventarioMaterialAdmin(admin.ModelAdmin):
    pass


admin.site.register(InventarioMaterial, InventarioMaterialAdmin)
