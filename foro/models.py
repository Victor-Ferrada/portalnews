from django.db import models

class Noticia(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField() ##para subir imagenes antes instalar pillow
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="New"
        verbose_name_plural="News"
    def __str__ (self):
        return "Titulo: "+self.title