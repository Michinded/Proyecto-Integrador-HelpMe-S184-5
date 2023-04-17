"""helpme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogs import views
#from blogs.views import RegistrarUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.register_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('', views.inicio, name='inicio'),
    path('foro/', views.foro, name='foro'),
    path('policies/', views.policies, name='policies'),
    path('about/', views.about, name='about'),
    path('foro/publicaciones/', views.publicaciones, name='publicaciones'),
    path('foro/perfil/', views.perfil, name='perfil'),
    path('registrarse/', views.registrarse, name='registrarse'),
    #path('registrarse/', RegistrarUsuario.as_view(), name='registrarse'),
]
