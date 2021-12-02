from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = ('username', 'matricula', 'saldo')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        if commit:
            user.save()
            return user


class UsuarioFormLog(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = ('matricula', 'username', 'password')

        widgets = {
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matrícula'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario', 'require pattern': "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"}),
            'password': forms.PasswordInput(attrs={'class': 'forms-control', 'placeholder': 'Contraseña'}),
        }

    def save(self, commit=True):
        user = super(UsuarioFormLog, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
