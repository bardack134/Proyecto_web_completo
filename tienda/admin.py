from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto





class CategoriaAdmin(admin.ModelAdmin):

    #estos campos habiamos determinado que se actualizarian automaticamente, por lo tanto seran solo Lectura 
	readonly_fields=('created', 'updated')
	

class ProductoAdmin(admin.ModelAdmin):

    #estos campos habiamos determinado que se actualizarian automaticamente, por lo tanto seran solo Lectura 
	readonly_fields=('created', 'updated')
	
	list_display=("nombre", "categoria", "precio" , "disponibilidad")


admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Producto, ProductoAdmin) 