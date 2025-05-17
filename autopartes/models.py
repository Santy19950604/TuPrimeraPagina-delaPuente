from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} - {self.nombre}"

class Autoparte(models.Model):
    numero_serie = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.numero_serie} - {self.descripcion[:20]}"