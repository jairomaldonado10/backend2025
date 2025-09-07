from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre","precio","descripcion","stock"]

    def clean_precio(self):
        v = self.cleaned_data["precio"]
        if v < 0: raise forms.ValidationError("El precio no puede ser negativo.")
        return v

    def clean_stock(self):
        v = self.cleaned_data["stock"]
        if v < 0: raise forms.ValidationError("El stock no puede ser negativo.")
        return v
