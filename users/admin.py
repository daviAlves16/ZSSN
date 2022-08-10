from django.contrib import admin
from .models import User, Itens, Inventario

# Register your models here.

@admin.register(Itens)
class ItensAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pontos')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo', 'latitude', 'longitude', 'contaminacao')
    
@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantidade')

