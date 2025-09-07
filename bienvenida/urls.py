from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('catalogo.urls')),     
    path('', lambda r: redirect('producto_list')),    
]
