from django.shortcuts import render

from blog.models import Post, Categoria

from django.contrib.auth.decorators import login_required

# Create your views here.

def blog(request):
    # Obtenemos todos los objetos "Post" de la base de datos.
    posts = Post.objects.all()
    
    # Obtenemos todas las categorías distintas de la base de datos.
    categorias = Categoria.objects.all().distinct()

    # Creamos un diccionario llamado "contexto" que contiene los posts y las categorías obtenidas.
    contexto = {'posts': posts, 'categorias': categorias}
    
    # Renderizamos la plantilla "blog.html" con el contexto proporcionado.
    return render(request, 'blog/blog.html', contexto)



def categoria(request, categoria_id):
    # Obtenemos la categoría correspondiente al "categoria_id" recibido como parámetro.
    categoria = Categoria.objects.get(id=categoria_id)
    
    # Obtenemos todos los posts que pertenecen a la categoría obtenida.
    posts = Post.objects.filter(categoria=categoria)
    
    # Creamos un diccionario llamado "contexto" con los posts y la categoría obtenida.
    contexto = {'posts': posts, 'categoria': categoria}
    
    # Renderizamos la plantilla "categoria.html" con el contexto proporcionado.
    return render(request, 'blog/categoria.html', contexto)




# def categoria(request, categoria_id):

    

#     categoria = Categoria.objects.get(id=categoria_id)

#     posts=Post.objects.filter(categoria=categoria)

#     contexto={'posts': posts, 'categorias': categoria}
    
#     return render(request, 'blog/categoria.html', contexto)

