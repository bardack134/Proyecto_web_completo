# Importamos los elementos necesarios de Django para manejar los formularios y la vista.
from django.contrib.auth import forms
from django.shortcuts import redirect, render

# Importamos el módulo para manejar mensajes
from django.contrib import messages

 # Importamos el formulario de autenticación
 #AuthenticationForm es una clase proporcionada por Django que se utiliza para crear un formulario de inicio de sesión en una aplicación web.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View

#la función logout que se utiliza para cerrar la sesión del usuario autenticado. 
from django.contrib.auth import login, logout, authenticate

# Importamos el formulario personalizado.
from .form import CustomUserCreationForm  

#TemplateView ya está diseñada para renderizar una plantilla específica cuando se accede a la vista. Aquí, template_name se establece en 'registro/gracias.html', lo que significa que cuando se acceda a esta vista, se renderizará la plantilla gracias.html.
from django.views.generic import TemplateView



# Creamos una vista basada en clase (VBC) llamada RegisterView que hereda de View.
class RegisterView(View):

    # Método GET para mostrar o crear el formulario de registro.
    def get(self, request):

        # Creamos una instancia del formulario personalizado.
        form = CustomUserCreationForm()  

        # Preparamos los datos del formulario para pasar al contexto.
        context = {
            'form': form 
        }

        # Mostramos la página de registro con el formulario.
        return render(request, 'registro/registro.html', context) 


    # Método POST para procesar los datos del formulario cuando se envía.
    def post(self, request):

        # Creamos una instancia del formulario con los datos del POST.
        form = CustomUserCreationForm(request.POST)  

        # Verificamos si los datos ingresados en el formulario son válidos.
        if form.is_valid():

          
            #para que el usuario logee automaticamente
            usuario=form.save()
            login(request, usuario)

            # Mostramos un mensaje de éxito.
            messages.success(request, 'Usuario registrado exitosamente.')  


            return redirect('gracias')  

        context = {
            # Preparamos los datos del formulario (incluso si no es válido) para pasar al contexto.
            'form': form  
        }

        #Mostramos la página de registro con el formulario y posibles errores.
        return render(request, 'registro/registro.html', context)  




# Creamos una vista llamada ThankYouView que hereda de TemplateView.
class ThankYouView(TemplateView):

    # Especificamos la plantilla que se utilizará para renderizar la vista.
    template_name = 'registro/gracias.html'


def cerrar_sesion(request):
    # Utilizamos la función logout() para cerrar la sesión del usuario.
    logout(request)

    # Redirigimos al usuario a la página de inicio ('home' es el nombre de la URL).
    return redirect('Home')


#página de inicio de sesión
def log(request):

    # Creamos una instancia del formulario de autenticación
    form = AuthenticationForm()  
    
    context = {
        # Agregamos el formulario al contexto para pasarlo a la plantilla
        'form': form  
    }

    
    # Renderizamos la plantilla "login.html" con el contexto proporcionado
    return render(request, 'login/login.html', context)  


# Creamos una vista basada en clase llamada LoginView, se usara para crear un formulario de login
class LoginView(View):  

    # Método GET para crear el formulario de inicio de sesión
    def get(self, request):  
        
    #AuthenticationForm es una clase proporcionada por Django que se utiliza para crear un formulario de inicio de sesión en una aplicación web.

        # Creamos una instancia del formulario de inicio de session
        form = AuthenticationForm() 

        # Preparamos el contexto con el formulario
        context = {'form': form}  

        # Renderizamos la plantilla con el contexto
        return render(request, 'login/login.html', context)  

    # Método POST para procesar los datos del formulario
    def post(self, request):  

        # Creamos una instancia del formulario de inicio de session pero con los datos POST
        form = AuthenticationForm(request, data=request.POST)  

        # Verificamos si el formulario es válido
        if form.is_valid():  

            # Obtenemos el nombre de usuario del formulario

            # En Django, después de que los datos ingresados por el usuario se someten al proceso de validación, se almacenan en el atributo cleaned_data, cleaned_data es un diccionario y usamos el metodo get() para obtener el valor del campo username
            nombre_usuario = form.cleaned_data.get("username")  

            # Obtenemos la contraseña del formulario
            contra = form.cleaned_data.get("password") 

            # Autenticamos al usuario

            #authenticate() verifica si las credenciales proporcionadas son válidas y corresponden a un usuario en la base de datos. Si las credenciales son válidas, devuelve un objeto de usuario. Si no son válidas, devuelve None.
            usuario = authenticate(username=nombre_usuario, password=contra) 

            # Si la autenticación fue exitosa
            if usuario is not None:  

                 # Iniciamos sesión para el usuario autenticado
                login(request, usuario) 

                
                return redirect('Home')
            
            # Si la autenticación falló 
            else:  

                # Mostramos un mensaje de error
                messages.error(request, "Usuario no válido")

        else:  # Si el formulario no es válido
            messages.error(request, "Información incorrecta")  # Mostramos un mensaje de error

        #todo lo anterior ocurre si el usario hace el proceso de logear, si no hace le proceso de logear salta directamente a estas dos ultimas lineas

        # Preparamos el contexto con el formulario (posiblemente con errores)
        context = {'form': form}  

        # Renderizamos la plantilla con el contexto
        return render(request, 'login/login.html', context)  