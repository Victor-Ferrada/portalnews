from django.shortcuts import render
from .models import Noticia

def noticia(request):
    noticias=Noticia.objects.all()
    return render(request,"foro/foro.html",{'noticias':noticias})