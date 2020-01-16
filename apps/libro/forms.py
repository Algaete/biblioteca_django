from django import forms
# .models el punto es para indicar q esta en la misma ruta
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad']
