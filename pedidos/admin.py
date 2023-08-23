# Importa el módulo admin de Django para administrar los modelos en el panel de administración
from django.contrib import admin
# Importa los modelos LineaPedido y Pedido desde el archivo models.py
from .models import Pedido



# Registra el modelo Pedido en el panel de administración
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):

    # Define los campos que se mostrarán en la lista de objetos de Pedido
    list_display = ('usuario', 'producto_nombre', 'cantidad', 'precio_total')
    
    # Define filtros que permiten filtrar los objetos de Pedido en el panel de administración
    list_filter = ('usuario',)
