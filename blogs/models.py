from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

# Create your models here.
def get_image_upload_path(instance, filename):
    return 'profile_pics/{}/{}'.format(instance.username, filename)

#Tabla de carreras
class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre_carrera = models.CharField(max_length=255)

#Tabla de usuarios
class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    fecha_nacimiento = models.DateField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    correo = models.CharField(max_length=255, primary_key=True)
    contrasena = models.CharField(max_length=255)
    foto_perfil = models.ImageField(storage=S3Boto3Storage(), upload_to=get_image_upload_path)
    strikes = models.IntegerField(default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)



class Pubs(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, default='anonymous')
    picture = models.ImageField(storage=S3Boto3Storage(), upload_to=get_image_upload_path)
    url_img = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.picture:
            self.url_img = self.picture.url
        super().save(*args, **kwargs)


