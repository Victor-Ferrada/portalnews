from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Noticia

def noticia(request):
    noticias=Noticia.objects.all()
    paginator = Paginator(noticias, 3)  # se cambia a noticaS para que sea iterable Y DE 3 POR PAGINA
    page_number = request.GET.get("page") 
    page_obj = paginator.get_page(page_number) 
    return render(request, "foro/foro.html", {"page_obj": page_obj}) 
