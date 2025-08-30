from django.http import HttpResponse

def inicio(request):
    nombre = "Jairo Maldonado"
    return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")