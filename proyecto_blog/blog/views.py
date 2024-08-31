from django.shortcuts import render, redirect
from .models import Post
from .forms import PostModelForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def ver_lista_publicaciones(request):
    query = request.GET.get('q')
    posts_list = Post.objects.all()

    if query:
        posts_list = posts_list.filter(Q(titulo__icontains=query)| Q(contenido__icontains=query)| Q(categoria__icontains=query))

    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'ver_lista_publicaciones.html', {'posts': posts})

def inicio(request):
    return render(request, 'inicio.html')

def agregar_publicacion(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(ver_lista_publicaciones)
    else:
        form = PostModelForm
    return render(request, 'agregar_publicacion.html', {'form': form})