# Importamos las funciones y clases necesarias desde el módulo django.shortcuts
from django.shortcuts import render

# Importamos los modelos Categoria y Producto definidos en el archivo models.py del mismo directorio
from .models import Categoria, Producto

from django.contrib.auth.decorators import login_required

# Definimos una función llamada "tienda" que manejará la lógica de la vista para la página de la tienda
@login_required
def tienda(request):
    
    # Obtenemos todos los objetos Producto de la base de datos y los almacenamos en la variable "productos"
    productos = Producto.objects.all()
    
    # Obtenemos todos los objetos Categoria de la base de datos y los almacenamos en la variable "categorias"
    categorias = Categoria.objects.all()

    # Creamos un diccionario llamado "contexto" que contendrá las variables "producto" y "categoria"
    # y sus respectivos valores obtenidos de la base de datos
    contexto = {'producto': productos, 'categoria': categorias}

    # Renderizamos la plantilla "tienda/tienda.html" y pasamos el diccionario "contexto" como contexto
    # para que las variables "producto" y "categoria" estén disponibles en la plantilla
    return render(request, 'tienda/tienda.html', contexto)
