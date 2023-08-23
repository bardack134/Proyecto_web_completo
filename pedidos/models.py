# Importa el módulo models de Django
from django.db import models

# Importa el modelo User de django.contrib.auth.models
from django.contrib.auth.models import User




# Define el modelo Pedido
class Pedido(models.Model):

    # Define una relación ForeignKey con el modelo User para representar el usuario que realizó el pedido

    #El campo usuario almacenará una clave foránea que hace referencia al ID del usuario en el modelo User
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # Define un campo CharField para almacenar el nombre del producto, con una longitud máxima de 255 caracteres
    producto_nombre = models.CharField(max_length=255)

    # Define un campo PositiveIntegerField para almacenar el ID del producto
    producto_id = models.PositiveIntegerField()

    # Define un campo PositiveIntegerField para almacenar la cantidad de productos en el pedido
    cantidad = models.PositiveIntegerField()

    # Define un campo DecimalField para almacenar el precio unitario del producto, con un máximo de 10 dígitos y 2 decimales
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    # Define un campo DecimalField para almacenar el precio total del pedido, con un máximo de 10 dígitos y 2 decimales
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    # Define el método __str__ para representar el objeto Pedido como una cadena
    def __str__(self):
        return f"Pedido de {self.usuario.username} - Producto: {self.producto_nombre}"

