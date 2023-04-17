from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import FileExtensionValidator
from .models import PerfilUsuario, Carrera
from django.core.exceptions import ValidationError

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nombre', 
        max_length=30, 
        widget=forms.TextInput(attrs={'class': 'form-control bg-secondary text-light'})
    )
    last_name = forms.CharField(
        label='Apellidos', 
        max_length=30, 
        widget=forms.TextInput(attrs={'class': 'form-control bg-secondary text-light'})
    )
    username = forms.CharField(
        label='Nombre de usuario', 
        max_length=150, 
        help_text='Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.', 
        widget=forms.TextInput(attrs={'class': 'form-control bg-secondary text-light'})
    )
    email = forms.EmailField(
        label='Correo electrónico', 
        max_length=254, 
        help_text='Se requiere una dirección de correo electrónico válida.', 
        widget=forms.EmailInput(attrs={'class': 'form-control bg-secondary text-light'})
    )
    password1 = forms.CharField(
        label='Contraseña', 
        strip=False, 
        widget=forms.PasswordInput(attrs={'class': 'form-control bg-secondary text-light'})
    )
    password2 = forms.CharField(
        label='Confirmar contraseña', 
        widget=forms.PasswordInput(attrs={'class': 'form-control bg-secondary text-light'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
        }

class RegistroExtra(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        label='Fecha de nacimiento',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control bg-secondary text-light'})
    )
    carrera = forms.ModelChoiceField(
        label='Carrera',
        queryset=Carrera.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control bg-secondary text-light'}),
        required=False,
    )
    foto_perfil = forms.ImageField(
        label='Foto de perfil',
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control bg-secondary text-light'}),
        required=False,
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
    )

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento and fecha_nacimiento >= date.today():
            raise ValidationError('La fecha de nacimiento debe ser anterior a la fecha actual')
        return fecha_nacimiento

    def clean_foto_perfil(self):
        foto_perfil = self.cleaned_data.get('foto_perfil')
        if foto_perfil:
            if foto_perfil.size > 1024*1024: # 1MB
                raise ValidationError('La foto de perfil debe tener un tamaño máximo de 1 MB')
        return foto_perfil

    class Meta:
        model = PerfilUsuario
        fields = ('fecha_nacimiento', 'carrera', 'foto_perfil',)
