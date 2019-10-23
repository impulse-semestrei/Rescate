from django.contrib import admin
from .models import Ambulancia

# Register your models here.

class AmbulanciaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ambulancia,AmbulanciaAdmin)
