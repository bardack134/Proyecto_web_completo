# Importa la función render, que se utiliza para renderizar una plantilla HTML con datos en Django.
from django.shortcuts import redirect, render

# Importa el modelo Pedido definido en el archivo models.py de la aplicación pedidos.
from pedidos.models import Pedido

# Importa el módulo "messages" para mostrar mensajes en la interfaz
from django.contrib import messages

# Importa la función send_mail y las configuraciones desde el archivo settings.py
from django.core.mail import send_mail
from django.conf import settings


#TemplateView ya está diseñada para renderizar una plantilla específica cuando se accede a la vista. Aquí, template_name se establece en 'registro/gracias.html', lo que significa que cuando se acceda a esta vista, se renderizará la plantilla gracias.html.
from django.views.generic import TemplateView


# Define una función llamada ver_pedidos que tomará un objeto request como parámetro.
def ver_pedidos(request):
    # Obtiene el usuario autenticado
    usuario_logueado = request.user
    
    # Obtén todos los pedidos del usuario logueado
    pedidos = Pedido.objects.filter(usuario=usuario_logueado)

    # Inicializa una cadena de texto para acumular la información de los pedidos
    mensaje_pedidos = ""

    # Recorre cada pedido individual en la lista de pedidos
    for pedido_individual in pedidos:
        # Aquí tienes acceso a los atributos de un pedido individual
        producto_id = pedido_individual.producto_id
        nombre_producto = pedido_individual.producto_nombre
        cantidad = pedido_individual.cantidad
        precio_unitario = pedido_individual.precio_unitario
        precio_total = pedido_individual.precio_total

        # Agrega la información del pedido actual a la cadena de texto
        mensaje_pedidos += f'Producto ID: {producto_id}\n'
        mensaje_pedidos += f'Nombre del producto: {nombre_producto}\n'
        mensaje_pedidos += f'Cantidad: {cantidad}\n'
        mensaje_pedidos += f'Precio unitario: {precio_unitario}\n'
        mensaje_pedidos += f'Precio total: {precio_total}\n\n'

    # Llama a la función enviar_email con los detalles de todos los pedidos
    enviar_email(
        nombre_usuario=request.user.username,
        email_usuario=request.user.email,
        mensaje_pedidos=mensaje_pedidos,
    )

    # Muestra un mensaje de éxito al usuario
    messages.success(request, "Los Pedidos se han creado correctamente")

    # Redirige al usuario a la página "Tienda"
    return redirect("pedido_procesado")

# Define una función llamada "enviar_email" que tomará varios parámetros relacionados con el pedido y el usuario
def enviar_email(nombre_usuario, email_usuario, mensaje_pedidos):
    # Asigna un asunto al correo
    subject = 'Nuevos pedidos realizados'
    
    # Crea el cuerpo del correo con los detalles de los pedidos y el nombre de usuario
    message = f'Hola {nombre_usuario}, se han realizado los siguientes pedidos:\n\n'
    message += mensaje_pedidos
    
    # Obtiene la dirección de correo electrónico del remitente desde la configuración
    from_email = settings.EMAIL_HOST_USER
    
    # Crea una lista de destinatarios, en este caso, solo el correo electrónico del usuario
    recipient_list = [email_usuario]

    # Utiliza la función send_mail para enviar el correo
    send_mail(subject, message, from_email, recipient_list)


# Creamos una vista llamada pedido_en_proceso que hereda de TemplateView.
class pedido_en_proceso(TemplateView):

    # Especificamos la plantilla que se utilizará para renderizar la vista.
    template_name = 'pedido/pedido.html'