from django.urls import path
from . import views

urlpatterns = [
    path("", views.productos_lista, name="producto_list"),
    path("crear/", views.producto_create, name="producto_create"),
    path("<int:pk>/", views.producto_detail, name="producto_detail"),
    path("<int:pk>/editar/", views.producto_update, name="producto_update"),
    path("<int:pk>/eliminar/", views.producto_delete, name="producto_delete"),
]
