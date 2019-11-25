from django.contrib import admin
from .models import Revision

# Register your models here.


class RevisionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Revision, RevisionAdmin)
