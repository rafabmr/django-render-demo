from django.contrib import admin
from .models import Usuarios

# Register your models here.
class UsuariosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'registro',
        'edad',
        'usuario',
        'contrasena',
    )
    list_filter = ('nombre','edad')

admin.site.register(Usuarios, UsuariosAdmin)