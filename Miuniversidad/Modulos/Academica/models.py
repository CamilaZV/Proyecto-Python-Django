from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0} (Duracion: {1} año(s))"
        return txt.format(self.nombre, self.duracion)

class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellido = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [('F','Femenino'),
             ('M','Masculino')]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)

    def nombreCompleto(self):
        txt = "{0}, {1}"
        return txt.format(self.apellido, self.nombre)  

    def __str__(self):
        txt = "{0} ({1}) / Carrera: {2} "  
        return txt.format(self.nombreCompleto(), self.dni, self.carrera)

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveBigIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0} ({1}) / Docente: {2}"
        return txt.format(self.nombre, self.codigo, self.docente)                       
    
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(null=False, blank=False, max_length=30)
