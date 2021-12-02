from django import forms
from .models import Operacion


class OperacionForm(forms.ModelForm):
    class Meta:
        model = Operacion

        fields = ('nombre', 'precio_unitario', 'cantidad', 'material')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'require pattern': "[a-zA-Z ]{2,254}"}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control', 'require pattern': "[a-zA-Z ]{2,254}"}),
            # 'fecha': forms.TextInput(attrs={'class':'form-control'}),
            # 'usuario': forms.TextInput(attrs={'class':'form-control'}),
        }
