from django.urls import path
from .views import ver_lista_publicaciones

urlpatterns = [
    path('posts/', ver_lista_publicaciones, name='ver_lista_publicaciones')
]