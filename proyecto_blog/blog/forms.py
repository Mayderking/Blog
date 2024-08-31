from django import forms
from .models import Post
from django.utils import timezone

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'categoria', 'autor']

    def clean_fecha_publicacion(self):
        fecha = self.cleaned_data.get('fecha_publicacion')
        if fecha > timezone.now().date():
            raise forms.ValidationError("Hermano usted es vidente o que?")
        return fecha
    
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if not titulo:
            raise forms.ValidationError("y el titulo que?")
        return titulo
        