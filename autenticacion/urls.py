from django.urls import path

#de las vistas importamos las clases que creamos
from .views import RegisterView, ThankYouView, cerrar_sesion, LoginView


urlpatterns = [
    # Asignamos la vista RegisterView a la URL raiz, con el nombre 'autenticacion'.
    path('', RegisterView.as_view(), name='autenticacion'),

    # Asignamos la función 'cerrar_sesion' a la URL 'cerrar/', con el nombre 'cerrar_sesion'.
    path('cerrar/', cerrar_sesion, name='cerrar_sesion'),

    

    path('login/', LoginView.as_view(), name='login'),
]


    

