# Importamos la función "render" desde el módulo django.shortcuts, la cual nos permite renderizar plantillas HTML con datos.
from django.shortcuts import render

# Importamos la clase "carrito" desde el archivo "carrito.py" que se encuentra en el mismo directorio.
from .carro import Carro

# Importamos el modelo "Producto" desde el archivo "models.py" del directorio "tienda".
from tienda.models import Producto

# Importamos la función "redirect" desde el módulo django.shortcuts, que nos permite redireccionar a una URL específica.
from django.shortcuts import redirect

# Importamos el modelo Pedido desde el archivo models.py en la app pedidos
from pedidos.models import Pedido 

from decimal import Decimal


from decimal import Decimal  # Importa la clase Decimal
from django.shortcuts import redirect
from pedidos.models import Pedido
# ...

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    
    # Llamamos al método "agregar_productos" del objeto "carro" y le pasamos el objeto "producto" como parámetro.
    carro.agregar(producto=producto)
    
    # Verificar si el producto ya existe en la base de datos de pedidos
    pedido_existente = Pedido.objects.filter(usuario=request.user, producto_id=producto.id).first()
    
    if pedido_existente:
        # Si el producto ya existe en la base de datos de pedidos, simplemente aumentamos la cantidad en 1 en el registro existente
        pedido_existente.cantidad += 1
        
        # Obtén el valor del precio del producto como Decimal
        precio_producto_decimal = Decimal(str(producto.precio))
        
        # Actualiza el precio total usando el valor en Decimal
        pedido_existente.precio_total += precio_producto_decimal
        pedido_existente.save()
    else:
        # Si el producto no existe en la base de datos de pedidos, crea un nuevo registro en el modelo Pedido
        Pedido.objects.create(
            usuario=request.user,
            producto_nombre=producto.nombre,
            producto_id=producto.id,
            cantidad=1,
            precio_unitario=producto.precio,
            precio_total=producto.precio,
        )
    
    return redirect('Tienda')


# Definimos la función "eliminar_producto" que se encargará de eliminar un producto del carrito de compras.
# Recibe el parámetro "request", que es el objeto que representa la solicitud HTTP recibida.
# También recibe el parámetro "producto_id", que es el ID del producto que se desea eliminar del carrito.
def eliminar_producto(request, producto_id):

    # Creamos un objeto "carro" de la clase "carrito" y le pasamos el objeto "request" como parámetro.
    carro = Carro(request)

    # Obtenemos el objeto "Producto" correspondiente al ID recibido como parámetro.
    #La línea de código producto = Producto.objects.get(id=producto_id) obtiene toda la información del producto correspondiente al ID recibido como parámetro.
    producto = Producto.objects.get(id=producto_id)

    # Llamamos al método "eliminar_producto" del objeto "carro" y le pasamos el objeto "Producto" como parámetro.
    # Este método eliminará el producto del carrito  de compras.
    carro.eliminar(producto=producto)

    # Eliminamos el registro en el modelo Pedido correspondiente al producto eliminado del carrito
    Pedido.objects.filter(usuario=request.user, producto_id=producto.id).delete()

    # Redireccionamos al usuario a la página de la tienda después de eliminar el producto.
    return redirect('Tienda')



# Definimos la vista 'restar_producto' que se ejecutará cuando un usuario quiera restar una unidad del producto en el carrito.
def restar_producto(request, producto_id):
    # Creamos una instancia de la clase 'carrito', pasando como parámetro el objeto 'request'.
    carro = Carro(request)

    # Obtenemos el objeto 'Producto' correspondiente al ID recibido como parámetro.
    producto = Producto.objects.get(id=producto_id)

    # Utilizamos el método 'restarUnidades()' de la clase 'carrito' para restar una unidad del producto en el carrito.
    carro.restar_producto(producto=producto)

    # Actualizamos la cantidad y el precio total en el registro del modelo Pedido correspondiente

    #En esta línea, usamos la función get() del modelo Pedido para obtener un registro específico de la base de datos que cumpla con dos condiciones: el usuario actual (request.user) y el ID del producto (producto.id). Esto  permite obtener el registro de un pedido específico relacionado con el usuario y el producto que  tratamos de restar del carrito.
    pedido = Pedido.objects.get(usuario=request.user, producto_id=producto.id)

    #Restar 1 a la cantidad en el registro del pedido
    pedido.cantidad -= 1

    # Obtén el valor del precio del producto como Decimal
    precio_producto_decimal = Decimal(str(producto.precio))

    # Restar el precio del producto al precio total en el registro del pedido
    pedido.precio_total -= precio_producto_decimal

    # Si la cantidad en el registro del pedido es igual a 0, eliminamos el registro
    if pedido.cantidad == 0:
        pedido.delete()
    else:
        pedido.save() 
    
    # Redirigimos al usuario a la página de la tienda después de restar la unidad del producto.
    return redirect('Tienda')


def limpiar_carro(request):
    # Creamos una instancia de la clase 'carrito', pasando como parámetro el objeto 'request'.
    carro = Carro(request)

    # Utilizamos el método 'limpiar_carro()' de la clase 'carrito' para eliminar todos los productos del carrito.
    carro.limpiar_carro()

    

    # Redirigimos al usuario a la página de la tienda después de limpiar el carrito.
    return redirect('Tienda')