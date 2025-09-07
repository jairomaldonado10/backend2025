from django.shortcuts import render
from .models import Producto

def productos_lista(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo/productos_lista.html', {'productos': productos})
