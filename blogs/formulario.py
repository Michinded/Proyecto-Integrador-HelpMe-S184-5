from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import FileExtensionValidator
from .models import PerfilUsuario, Carrera
from django.core.exceptions import ValidationError

class RegistroForm(UserCreationForm):

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
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    carrera = forms.ModelChoiceField(
        label='Carrera',
        queryset=Carrera.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control bg-secondary text-light'}),
        required=False,
    )
    foto_perfil = forms.ImageField(
        label='Foto de perfil',
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control-file'}),
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
