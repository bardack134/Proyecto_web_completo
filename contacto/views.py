from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.core.mail import send_mail, BadHeaderError, EmailMessage

from .form import FormularioContacto
# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method == "POST":

        formulario_contacto=FormularioContacto(request.POST)

        # check whether it's valid:
        if formulario_contacto.is_valid():

            # process the data in form.cleaned_data as required
            nombre=formulario_contacto.cleaned_data["nombre"]

            email=formulario_contacto.cleaned_data["email"]

            contenido=formulario_contacto.cleaned_data["contenido"]
           
            email = EmailMessage(
            "mensaje desde app Django",
            f"el usuario {nombre} con el email {email} te envia el siguiente mensaje: \n\n {contenido}",
            "",
            ["bardack134@gmail.com",],
            reply_to=[email],
            )
            
            try:
                email.send()

                # redirect to a new URL:
                return redirect("/contacto/?gracias")
            
            
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            
            except:
                
                return redirect("/contacto/?novalido")
    
    

    contexto={'miformulario':formulario_contacto}

    return render(request, 'contacto/contacto.html', contexto)

    
      
        