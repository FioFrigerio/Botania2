from django.contrib import admin
from .models import Usuario, tipo_usuario, Catalogo
# Register your models here.

admin.site.register(tipo_usuario)
admin.site.register(Usuario) 
admin.site.register(Catalogo) 