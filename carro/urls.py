# Importamos la función "path" desde el módulo django.urls, que nos permite definir las rutas de URL en nuestra aplicación.
from django.urls import path

# Importamos las vistas (funciones) definidas en el archivo "views.py" de la misma aplicación.
from . import views

app_name = 'carro'

# Definimos una lista llamada "urlpatterns" que contendrá todas las rutas de URL de nuestra aplicación.
urlpatterns = [
    
    # La siguiente ruta de URL se define como 'agregar/<int:producto_id>/', y está asociada a la vista "views.agregar_producto".
    # Cuando un usuario accede a la URL "agregar/<int:producto_id>/", se ejecutará la función "agregar_producto" en el archivo "views.py".
    # El parámetro "producto_id" es un entero que será pasado como argumento a la función "agregar_producto".
    # Además, se asigna el nombre 'agregar' a esta ruta de URL, que puede ser usado para referenciarla en otros lugares del código.
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),

    # La siguiente ruta de URL se define como 'eliminar/<int:producto_id>/', y está asociada a la vista "views.eliminar_producto".
    # Cuando un usuario accede a la URL "eliminar/<int:producto_id>/", se ejecutará la función "eliminar_producto" en el archivo "views.py".
    # El parámetro "producto_id" es un entero que será pasado como argumento a la función "eliminar_producto".
    # Además, se asigna el nombre 'eliminar' a esta ruta de URL, que puede ser usado para referenciarla en otros lugares del código.
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),

    # La siguiente ruta de URL se define como 'restar/<int:producto_id>/', y está asociada a la vista "views.restar_producto".
    # Cuando un usuario accede a la URL "restar/<int:producto_id>/", se ejecutará la función "restar_producto" en el archivo "views.py".
    # El parámetro "producto_id" es un entero que será pasado como argumento a la función "restar_producto".
    # Además, se asigna el nombre 'restar' a esta ruta de URL, que puede ser usado para referenciarla en otros lugares del código.
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),

    # La siguiente ruta de URL se define como 'limpiar/', y está asociada a la vista "views.limpiar_carro".
    # Cuando un usuario accede a la URL "limpiar/", se ejecutará la función "limpiar_carro" en el archivo "views.py".
    # No hay parámetros adicionales en esta ruta.
    # Además, se asigna el nombre 'limpiar' a esta ruta de URL, que puede ser usado para referenciarla en otros lugares del código.
    path('limpiar/', views.limpiar_carro, name='limpiar'),
    
    # Otras rutas de URL pueden agregarse aquí si es necesario, cada una asociada a una vista y con su respectivo nombre asignado.
]
