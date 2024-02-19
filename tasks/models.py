from django.db import models

# Create your models here. Se crean las TABLAS de BD
#Tabla Sobrepeso
class Sobrepeso(models.Model):
    id_sobrepeso = models.AutoField(primary_key=True)
    tipo= models.CharField(max_length=20)
    estilo_vida = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.tipo +'_'+ self.estilo_vida

#Tabla Localidad
class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    cp = models.CharField(max_length=5)
    estrato = models.CharField(max_length=20)
    region_ensanut = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.cp+'_'+ self.estrato

#Tabla Curso
class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=20)
    grado = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.nombre_curso+'_'+ self.grado 

#Tabla Usuario
class Task(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    estatura = models.DecimalField(max_digits=4,decimal_places=1)
    talla = models.CharField(max_length=20)
    peso = models.DecimalField(max_digits=5,decimal_places=2)
    imc = models.DecimalField(max_digits=3,decimal_places=1)
    actividad_fisica = models.BooleanField(default=False)
    id_sobrepeso = models.ForeignKey(Sobrepeso, on_delete=models.CASCADE,blank=True, null=True)
    cp = models.ForeignKey(Localidad, on_delete=models.CASCADE,blank=True, null=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self) -> str:
        return self.matricula +'_'+ self.nombre








