# Importamos la clase de formularios de Django
from django import forms  

# Importamos el modelo de usuario de Django
from django.contrib.auth.models import User 

# Importamos el formulario de creación de usuario de Django
from django.contrib.auth.forms import UserCreationForm 

# Importamos la excepción de validación de Django
from django.core.exceptions import ValidationError  


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CustomUserCreationForm(UserCreationForm):

    # Definimos un campo de entrada para el nombre de usuario con longitud mínima de 5 y máxima de 150 caracteres.
    username = forms.CharField(label='username', min_length=5, max_length=150)

    # Definimos un campo de entrada para el correo electrónico.
    email = forms.EmailField(label='email')

    # Definimos un campo de contraseña con etiqueta "password" y widget de contraseña (oculto).

    #l "widget" se refiere a la representación visual y de interacción de un campo de formulario en la interfaz de usuario de una página web. Ayuda a definir cómo se mostrará y se comportará el campo para que los usuarios puedan interactuar con él de manera adecuada.
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)

    # Definimos un campo para confirmar la contraseña, también oculto.
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    # Método para validar el nombre de usuario (lowercase) y verificar si ya existe en la base de datos.
    def username_clean(self):

        # Obtenemos el valor ingresado en el campo 'username' y lo convertimos a minúsculas.

        #con la funcion clean_data se hace el proceso de validacion y el valor queda guardado dentro de clean_data que es un diccionario
        username = self.cleaned_data['username'].lower()

        # Consultamos si ya existe un usuario con el mismo nombre de usuario.
        new = User.objects.filter(username=username)


       # Verificamos si ya existe un usuario con el mismo nombre de usuario o correo electrónico en la base de datos.
        if new.count():  # Si new.count() devuelve un número mayor que 0 (verdadero).

            # Si ya existe al menos un usuario con la misma información, lanzamos una excepción.
            raise ValidationError("User Already Exists")
        

        # Si no existe un usuario con la misma información, procedemos a retornar el nombre de usuario.
        return username


    # Método para validar el correo electrónico y verificar si ya existe en la base de datos.
    def clean_email(self):
        # Obtenemos el valor ingresado en el campo 'email' y lo convertimos a minúsculas.
        email = self.cleaned_data['email'].lower()

        # Consultamos si ya existe un usuario con el mismo correo electrónico.
        new = User.objects.filter(email=email)

        if new.count():  # Si new.count() devuelve un número mayor que 0 (verdadero).

            raise ValidationError("Email Already Exists")  # Lanzamos una excepción si ya existe un usuario con el mismo correo electrónico.
        
        return email  # Si no existe un usuario con el mismo correo electrónico, devolvemos el correo electrónico para su uso en el proceso de registro.


    # Método para validar que las contraseñas coincidan.
    def clean_password2(self):

        # Obtenemos los valores ingresados en los campos de contraseña.
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        #  Esta expresión evalúa tres condiciones. En primer lugar, verifica si password1 es verdadero (es decir, no es una cadena vacía o nula), luego verifica si password2 es verdadero y finalmente compara si las contraseñas no coinciden. Si alguna de las condiciones no se cumple, el bloque de código no se ejecutará. Esto significa que si password1 o password2 es una cadena vacía o nula, el bloque no se ejecutará, lo cual no es el comportamiento deseado.
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords Don't Match")  # Lanzamos una excepción si no coinciden.
        return password2



    # Este método save se encarga de crear y guardar un nuevo usuario en la base de datos utilizando los datos ingresados en el formulario

    #El argumento commit tiene un valor predeterminado de True, lo que indica que, por defecto, se guardará el objeto en la base de datos cuando se cree.
    def save(self, commit=True):

        # Creamos un nuevo usuario utilizando los datos ingresados.

        #create_user es un método proporcionado por Django que crea un nuevo usuario y almacena la información necesaria en la base de datos.
        user = User.objects.create_user(

            #Estos son los valores limpios y validados de los campos del formulario. cleaned_data es un diccionario que contiene los valores de los campos después de pasar por la validación. Estamos pasando estos valores directamente a create_user para crear el nuevo usuario.
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )

        #Finalmente, se devuelve el objeto del usuario recién creado. Esto puede ser útil si deseas hacer algo con el usuario después de haberlo creado, como redireccionar a una página de inicio de sesión o mostrar un mensaje de éxito
        return user
