from django.urls import path
from .views import ver_lista_publicaciones, agregar_publicacion, editar_publicacion,detalles_publicacion

urlpatterns = [
    path('posts/', ver_lista_publicaciones, name='ver_lista_publicaciones'),
    path('agregar_publicacion/', agregar_publicacion, name='agregar_publicacion'),
    path('editar_publicacion/<int:post_id>', editar_publicacion, name='editar_publicacion'),
    path('detalles_publicacion<int:post_id>/', detalles_publicacion, name='detalles_publicacion'),
]