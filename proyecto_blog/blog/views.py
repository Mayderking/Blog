from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostModelForm
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime

# Create your views here.

def ver_lista_publicaciones(request):
    query = request.GET.get('q')
    inicio_fecha = request.GET.get('inicio_fecha')
    final_fecha = request.GET.get('final_fecha')
    posts_list = Post.objects.all()

    if query:
        posts_list = posts_list.filter(Q(titulo__icontains=query)| Q(contenido__icontains=query)| Q(categoria__icontains=query))

    if inicio_fecha:
        try:
            inicio_fecha = datetime.strptime(inicio_fecha, '%Y-%m-%d')
            posts_list = posts_list.filter(fecha_publicacion__gte=inicio_fecha)
        except ValueError:
            pass

    if final_fecha:
        try:
            final_fecha = datetime.strptime(final_fecha, '%Y-%m-%d')
            posts_list = posts_list.filter(fecha_publicacion__lte=final_fecha)
        except ValueError:
            pass

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

def editar_publicacion(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('ver_lista_publicaciones')
    else:
        form = PostModelForm(instance=post)
    return render(request, 'editar_publicacion.html', {'form': form, 'post': post})

def detalles_publicacion(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detalles_publicacion.html', {'post': post})
