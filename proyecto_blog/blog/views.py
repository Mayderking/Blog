from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def ver_lista_publicaciones(request):
    posts = Post.objects.all()
    return render(request, 'ver_lista_publicaciones.html', {'posts': posts})

def inicio(request):
    return render(request, 'inicio.html')