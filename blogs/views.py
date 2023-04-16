from django.shortcuts import render
from datetime import datetime
from .models import Pubs
from django.shortcuts import redirect
from .models import Usuario, Carrera
#from django.http import HttpResponse

# Create your views here.
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
        foto_perfil = request.FILES.get('profile_pic')

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

        # Redirigir al usuario a una página de éxito
        return redirect('foro')

    else:
        year = datetime.now().year
        return render(request, 'signup.html', {'year': year})

def login_user(request):
    if 'usuario_id' in request.session:
        return redirect('foro')
    year = datetime.now().year
    return render(request, 'login.html', {'year': year})

def inicio(request):
    if 'usuario_id' in request.session:
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

def perfil(request):
    year = datetime.now().year
    #if 'usuario_id' not in request.session:
        #return redirect('inicio')
    #usuario_id = request.session['usuario_id']
    #usuario = Usuario.objects.get(id=usuario_id)
    pubs = Pubs.objects.all()
    usuario = Usuario.objects.all()
    carrera = Carrera.objects.all()
    return render(request, 'perfil.html', {'year': year, 'pubs': pubs, 'usuario': usuario, 'carrera': carrera})
