from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

def productos_lista(request):
    productos = Producto.objects.all()
    return render(request, "catalogo/productos_lista.html", {"object_list": productos})


def producto_detail(request, pk):
    obj = get_object_or_404(Producto, pk=pk)
    return render(request, "catalogo/producto_detail.html", {"object": obj})


def producto_create(request):
    form = ProductoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("producto_list")
    return render(request, "catalogo/producto_form.html", {"form": form})


def producto_update(request, pk):
    obj = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("producto_list")
    return render(request, "catalogo/producto_form.html", {"form": form})


def producto_delete(request, pk):
    obj = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("producto_list")
    return render(request, "catalogo/producto_confirm_delete.html", {"object": obj})
