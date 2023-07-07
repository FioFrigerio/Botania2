from .models import Usuario, tipo_usuario, Catalogo
from django.forms import ModelForm


class usuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"


class tipo_usuarioForm(ModelForm):
    class Meta:
        model = tipo_usuario
        fields = [
            "tipo_usuario",
        ]
        labels = {
            "tipo_usuario": "tipo_usuario",
        }

class catalogoForm(ModelForm):
    class Meta:
        model = Catalogo
        fields = "__all__"
