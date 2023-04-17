from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from storages.backends.s3boto3 import S3Boto3Storage
import uuid

# Create your models here.
def get_image_upload_path(instance, filename):
    return 'profile_pics/{}/{}'.format(instance.username, filename)


def get_image_upload_path2(instance, filename):
    return 'profile_pics/{}/{}'.format(instance.user.username, filename)

#Tabla de carreras
class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre_carrera = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_carrera

#Tabla de datos extra de usuarios
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to=get_image_upload_path2, null=True, blank=True)


class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    fecha_nacimiento = models.DateField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    correo = models.CharField(max_length=255, unique=True)
    contrasena = models.CharField(max_length=255)
    foto_perfil = models.ImageField(storage=S3Boto3Storage(), upload_to=get_image_upload_path)
    strikes = models.IntegerField(default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)




class Pubs(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, default='anonymous')
    picture = models.ImageField(storage=S3Boto3Storage(), upload_to=get_image_upload_path)
    url_img = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.picture:
            self.url_img = self.picture.url
        super().save(*args, **kwargs)

class Imagenes(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='profile_pics/')
    picture_url = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.picture:
            # Obtener la extensión del archivo
            file_extension = self.picture.content_type.split('/')[-1]
            # Renombrar el archivo antes de subirlo a S3
            filename = f"{self.name}-profile-photo.{file_extension}"
            self.picture.name = filename

         # Subir el archivo a S3 y guardar la URL en el campo picture_url
            storage = self.picture.storage
            url = storage.save(self.picture.name, self.picture)
            self.picture_url = storage.url(url)

        super().save(*args, **kwargs)


class Profiles(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='profile_pics/')
    picture_url = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.picture:
            # Renombrar el archivo antes de subirlo a S3
            filename = f"{self.name}-profile-photo.png"
            self.picture.name = filename

            # Obtener el tipo de archivo a partir de la extensión
            extension = self.picture.name.split('.')[-1]
            if extension in ['png', 'jpg', 'jpeg', 'gif']:
                content_type = f"image/{extension}"
            else:
                content_type = None
        
            # Subir el archivo a S3 y guardar la URL en el campo picture_url
            storage = self.picture.storage
            url = storage.save(self.picture.name, self.picture)
            self.picture_url = storage.url(url)
        
            # Asignar el tipo de archivo al objeto
            self.picture.content_type = content_type

        super().save(*args, **kwargs)

        super().save(*args, **kwargs)
