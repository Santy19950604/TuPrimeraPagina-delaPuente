from ckeditor.fields import RichTextField
from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Marcas"


class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} - {self.nombre}"

    class Meta:
        verbose_name_plural = "Modelos"


class Autoparte(models.Model):
    numero_serie = models.CharField(max_length=100, unique=True)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to="autopartes/", blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.numero_serie} - {self.descripcion[:20]}"

    class Meta:
        verbose_name_plural = "Autopartes"
