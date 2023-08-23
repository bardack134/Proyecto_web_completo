# Importamos la clase "Carro" desde el archivo "carro.py" que se encuentra en el mismo directorio.
from .carro import Carro

# Definimos una función llamada "importe_total_carro" que recibe un objeto "request" como parámetro.
def importe_total_carro(request):
    
    # Creamos un objeto "carro" de la clase "Carro" y le pasamos el objeto "request" como parámetro.
    # Esto nos permite acceder a la sesión y mantener el carrito de compras entre las solicitudes HTTP.
    carro = Carro(request)

    # Inicializamos la variable "total" en 0. Esta variable se utilizará para almacenar el importe total del carrito.
    total = 0

    # Verificamos si el usuario actual está autenticado. 
    # request.user.is_authenticated es una propiedad que devuelve True si el usuario está autenticado y False si no lo está.
    #
    if request.user.is_authenticated:

        # Si el usuario está autenticado, recorremos todos los elementos del carrito que se encuentran en la sesión del usuario (request.session["carro"]).
        
        for key, value in request.session["carro"].items():
            # Calculamos el precio total para cada producto en el carrito. Multiplicamos el precio delproducto por la cantidad de unidades en el carrito y lo sumamos al total.
            total = total + float(value["precio"])
    
    # Finalmente, devolvemos un diccionario con la clave "importe_total_carro" que contiene el valor total calculado.
    return {"importe_total_carro": total}
