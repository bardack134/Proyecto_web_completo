# Importamos el módulo "models" de Django, que nos permite definir los modelos de la base de datos.
from django.db import models

# Definimos el modelo "Categoria" que representa una categoría de productos en la tienda.
class Categoria(models.Model):

    # Definimos un campo "nombre" de tipo CharField que almacenará el nombre de la categoría.
    nombre = models.CharField(max_length=50)
    
    # Definimos un campo "created" de tipo DateTimeField que almacenará la fecha y hora de creación de la categoría.
    created = models.DateTimeField(auto_now_add=True)
    
    # Definimos un campo "updated" de tipo DateTimeField que almacenará la fecha y hora de la última actualización de la categoría.
    updated = models.DateTimeField(auto_now_add=True)

    # Clase Meta que contiene metadatos sobre el modelo "Categoria".
    class Meta:
        # Definimos el nombre en singular que se utilizará para mostrar el modelo en el administrador de Django.
        verbose_name = 'categoriapro'

        # Definimos el nombre en plural que se utilizará para mostrar varios objetos del modelo en el administrador de Django.
        verbose_name_plural = 'categoriasprod'

    # Método "__str__" que define cómo se mostrará el objeto "Categoria" cuando se convierta a cadena.
    def __str__(self):
        return self.nombre


# Definimos el modelo "Producto" que representa un producto en la tienda.
class Producto(models.Model):

    # Definimos un campo "nombre" de tipo CharField que almacenará el nombre del producto.
    nombre = models.CharField(max_length=30)
    
    # Definimos un campo "categoria" de tipo ForeignKey que establecerá una relación con el modelo "Categoria".
    # El parámetro "on_delete=models.CASCADE" indica que si se elimina una categoría, los productos asociados también se eliminarán.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # Definimos un campo "imagen" de tipo ImageField que almacenará la imagen del producto.
    # El parámetro "upload_to='tienda'" indica que las imágenes se guardarán en la carpeta "tienda" del directorio de medios.
    # Los parámetros "null=True, blank=True" permiten que el campo sea opcional y pueda estar vacío.
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
       
    # Definimos un campo "precio" de tipo FloatField que almacenará el precio del producto.
    precio = models.FloatField(max_length=30)
    
    # Definimos un campo "disponibilidad" de tipo BooleanField que indicará si el producto está disponible o no.
    # Por defecto, el valor será True, lo que significa que el producto está disponible.
    disponibilidad = models.BooleanField(default=True)

    # Definimos un campo "created" de tipo DateTimeField que almacenará la fecha y hora de creación del producto.
    created = models.DateTimeField(auto_now_add=True)
    
    # Definimos un campo "updated" de tipo DateTimeField que almacenará la fecha y hora de la última actualización del producto.
    updated = models.DateTimeField(auto_now_add=True)

    # Clase Meta que contiene metadatos sobre el modelo "Producto".
    class Meta:

        # Definimos el nombre en singular que se utilizará para mostrar el modelo en el administrador de Django.
        verbose_name = 'Producto'

        # Definimos el nombre en plural que se utilizará para mostrar varios objetos del modelo en el administrador de Django.
        verbose_name_plural = 'Productos'
    
    
