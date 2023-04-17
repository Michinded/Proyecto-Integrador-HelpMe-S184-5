from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .models import Carrera, PerfilUsuario
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
#from django.http import HttpResponse
#from .models import Usuario
from blogs.formulario import RegistroForm, RegistroExtra
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def encriptar_contrasena(contrasena):
    return contrasena

# Clase registrarse
"""
class RegistrarUsuario(CreateView):
    model = User
    template_name = "registrarse.html"
    form_class = RegistroForm
    success_url = "/foro"
"""
def registrarse(request):
    if request.user.is_authenticated:
        return redirect('foro')
    year = datetime.now().year
    form = RegistroForm()
    extraf = RegistroExtra()
    if request.method == 'GET':
        return render(request, 'registrarse.html', {'form': form, 'year': year, 'error': '', 'extraf': extraf})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                username = request.POST['username']
                email = request.POST['email']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                password = request.POST['password1']

                # Verificar si el correo electrónico ya está en uso
                if User.objects.filter(email=email).exists():
                    formm = RegistroForm(request.POST)
                    return render(request, 'registrarse.html', {'error': 'El correo electrónico ya está en uso', 'year': year, 'form': formm, 'extraf': extraf})

                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password
                )
                user.save()
                login(request, user)
                foto_perfil = request.FILES.get('foto_perfil')
                carrera_id = request.POST.get('carrera')
                fecha_nacimiento = request.POST.get('fecha_nacimiento')

                infoextra = PerfilUsuario(
                    user_id=user.id,
                    foto_perfil=foto_perfil,
                    carrera_id=carrera_id,
                    fecha_nacimiento=fecha_nacimiento,
                )
                infoextra.save()

                return redirect('foro')
            except IntegrityError:
                form2 = RegistroForm(request.POST)
                return render(request, 'registrarse.html', {'error': 'El nombre de usuario ya existe', 'year': year, 'form': form2, 'extraf': extraf})
        else:
            form3 = RegistroForm(request.POST)
            return render(request, 'registrarse.html', {'error': 'Las contraseñas no coinciden', 'year': year, 'form': form3, 'extraf': extraf})
        



# Create your views here.
"""
def register_user(request):
    if 'usuario_id' in request.session:
        return redirect('foro')
    if request.method == 'POST':
        nombre = request.POST.get('name')
        apellidos = request.POST.get('last_name')
        username = request.POST.get('username')
        fecha_nacimiento = request.POST.get('birth_date')
        carrera_id = request.POST.get('carrera')
        correo = request.POST.get('email')
        contrasena = request.POST.get('password1')
        contrasena2 = request.POST.get('password2')
        foto_perfil = request.FILES.get('profile_pic')

        try:
            # Validar que las contraseñas sean iguales
            if contrasena != contrasena2:
                raise ValueError("Las contraseñas no coinciden")

            # Validar que el username o el correo no estén registrados
            if Usuario.objects.filter(Q(username=username) | Q(correo=correo)).exists():
                raise ValueError("El nombre de usuario o el correo ya está registrado")

            # Guardar objeto Carrera
            carrera = Carrera.objects.get(pk=carrera_id)

            # Guardar objeto Usuario
            usuario = Usuario(
                nombre=nombre,
                apellidos=apellidos,
                username=username,
                fecha_nacimiento=fecha_nacimiento,
                carrera=carrera,
                correo=correo,
                contrasena=contrasena,
                foto_perfil=foto_perfil,
            )
            usuario.save()
            request.session['usuario_id'] = usuario.usuario_id
            login(request, usuario)

            print("El usuario se ha guardado correctamente:", usuario)

            # Redirigir al usuario a una página de éxito
            return redirect('foro')

        except ValueError as e:
            # Enviar el error a la vista
            year = datetime.now().year
            return render(request, 'signup.html', {'error': str(e), 'year': year})

    else:
        year = datetime.now().year
        return render(request, 'signup.html', {'year': year})
"""
def login_user(request):
    if request.user.is_authenticated:
        return redirect('foro')
    year = datetime.now().year
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        # Autenticar el usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si el usuario se autentica correctamente, iniciar sesión
            login(request, user)

            if remember:
                # Si se seleccionó "Recuérdame", establecer una cookie para mantener la sesión iniciada
                request.session.set_expiry(1209600)  # 2 semanas de duración
            else:
                # Si no se seleccionó "Recuérdame", cerrar la sesión cuando se cierre el navegador
                request.session.set_expiry(0)

            # Redirigir al usuario a la página de inicio después de iniciar sesión
            return redirect('foro')
        else:
            # Si la autenticación falla, mostrar un mensaje de error
            error = 'El nombre de usuario o la contraseña son incorrectos.'
            return render(request, 'login.html', {'error': error, 'year': year})
    else:
        # Si la solicitud no es POST, mostrar la página de inicio de sesión
        return render(request, 'login.html', {'year': year, 'error': ''})


def signout(request):
    logout(request)
    return redirect('inicio')


def inicio(request):
    if request.user.is_authenticated:
        return redirect('foro')
    year = datetime.now().year
    return render(request, 'inicio.html', {'year': year})

def foro(request):
    year = datetime.now().year
    return render(request, 'foro.html', {'year': year})


def policies(request):
    year = datetime.now().year
    return render(request, 'policies.html', {'year': year})

def about(request):
    year = datetime.now().year
    return render(request, 'about.html', {'year': year})

def publicaciones(request):
    year = datetime.now().year
    return render(request, 'publicaciones.html', {'year': year})

@login_required
def perfil(request):
    year = datetime.now().year
    #if 'usuario_id' not in request.session:
        #return redirect('inicio')
    #usuario_id = request.session['usuario_id']
    #usuario = Usuario.objects.get(id=usuario_id)
    #pubs = Pubs.objects.all()
    usuario = User.objects.all()
    carrera = Carrera.objects.all()
    return render(request, 'perfil.html', {'year': year, 'usuario': usuario, 'carrera': carrera})
