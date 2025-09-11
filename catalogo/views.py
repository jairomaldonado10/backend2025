from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Producto
from .forms import ProductoForm

def productos_lista(request):
    productos = Producto.objects.all().order_by('id')
    return render(request, "catalogo/productos_lista.html", {"object_list": productos})

def producto_detail(request, pk):
    obj = get_object_or_404(Producto, pk=pk)
    return render(request, "catalogo/producto_detail.html", {"object": obj})

def producto_create(request):
    form = ProductoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado correctamente.")
            return redirect("producto_list")
        messages.error(request, "Revisa los errores del formulario.")
    return render(request, "catalogo/producto_form.html", {"form": form})

def producto_update(request, pk):
    obj = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, instance=obj)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado.")
            return redirect("producto_list")
        messages.error(request, "Revisa los errores del formulario.")
    return render(request, "catalogo/producto_form.html", {"form": form})

@csrf_protect
@require_POST
def producto_delete(request, pk):
    obj = get_object_or_404(Producto, pk=pk)
    obj.delete()
    # Si la petición es AJAX, respondemos JSON
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"ok": True})
    # Si es un form normal, redirigimos con mensaje
    messages.success(request, "Producto eliminado.")
    return redirect("producto_list")
