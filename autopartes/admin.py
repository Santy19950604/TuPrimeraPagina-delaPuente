from django.contrib import admin
from .models import Marca, Modelo, Autoparte

admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Autoparte)

# Register your models here.
