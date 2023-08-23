from django.urls import path

from . import views

#de las vistas importamos las clases que creamos
from .views import pedido_en_proceso
urlpatterns = [
        
    
    path('', views.ver_pedidos, name='procesar_pedido'),
    
    path('pedido_procesado/', views.pedido_en_proceso.as_view(), name='pedido_procesado'),  # Cambia la ruta para el pedido procesado

]