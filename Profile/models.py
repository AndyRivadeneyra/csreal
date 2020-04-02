from django.db import models
from django.utils import timezone

# Create your models here.
class modeloEstadoCivil(models.Model):
    estado = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.estado

    class Meta:
        db_table = 'EstadoCivil'

class modeloEstado(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Estado'

class modeloOcupacion(models.Model):
    ocupacion = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ocupacion

    class Meta:
        db_table = 'Ocupacion'

class modeloGenero(models.Model):
    sexo = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sexo

    class Meta:
        db_table = 'Genero'

class modeloCiudad(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Ciudad'

class modeloProfile(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apellidoMaterno = models.CharField(max_length=254, null=False)
    apellidoPaterno = models.CharField(max_length=254, null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.ForeignKey(modeloCiudad,on_delete=models.CASCADE)
    genero = models.ForeignKey(modeloGenero,on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(modeloOcupacion,on_delete=models.CASCADE)
    estado = models.ForeignKey(modeloEstado,on_delete=models.CASCADE)
    estadoCivil = models.ForeignKey(modeloEstadoCivil,on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'modeloProfile'