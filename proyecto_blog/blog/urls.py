from django.urls import path
from .views import ver_lista_publicaciones, agregar_publicacion

urlpatterns = [
    path('posts/', ver_lista_publicaciones, name='ver_lista_publicaciones'),
    path('agregar_publicacion/', agregar_publicacion, name='agregar_publicacion'),
]