from django.contrib import admin
from .models import Pubs
from .models import Carrera
from .models import Usuario

# Register your models here.
admin.site.register(Pubs)
admin.site.register(Carrera)
admin.site.register(Usuario)