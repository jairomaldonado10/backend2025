from django.contrib import admin
from django.urls import path
from catalogo.views import productos_lista  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', productos_lista, name='productos_lista'),
    path('', productos_lista), 
]
