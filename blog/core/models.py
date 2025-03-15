
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"

class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    profesor = models.CharField(max_length=100)
    estudiantes = models.CharField(max_length=100)
    numero_curso = models.IntegerField(max_length=100)
    fecha_inicio = models.DateField(max_length=100)
    fecha_fin = models.DateField(max_length=100)

    def __str__(self):
        return f"curso: {self.nombre} \n profesor: {self.profesor} \n comision: {self.numero_curso} \n fecha inicio: {self.fecha_inicio} \n fecha fin: {self.fecha_fin}"


