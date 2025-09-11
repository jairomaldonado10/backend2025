from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "stock", "activo"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej: Cargador iPhone 20W"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "stock": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
