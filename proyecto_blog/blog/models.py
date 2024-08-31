from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)

    def __str__(self):
        return str(self.titulo)
    