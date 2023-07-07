from django.db import models

# Create your models here.

class tipo_usuario(models.Model):
    idtipo_usuario = models.AutoField(
        primary_key=True, db_column='idtipo', verbose_name='id_tipo_usuario'
    )
    tipo_usuario = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipo_usuario)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apaterno = models.CharField(max_length=30, blank=False, null=False)
    amaterno = models.CharField(max_length=30, blank=False, null=False)
    correo = models.EmailField(unique=True, blank=False, null=False, max_length=100)
    clave = models.CharField(max_length=30, blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    region = models.CharField(max_length=50, blank=False, null=False)
    provincia = models.CharField(max_length=50, blank=False, null=False)
    comuna = models.CharField(max_length=50, blank=False, null=False)
    codpos = models.CharField(max_length=7, blank=False, null=False)
    tipo_usuario = models.ForeignKey(tipo_usuario, on_delete=models.CASCADE, db_column='idtipo')

    def __str__(self):
        return str(self.nombre) + " " + str(self.apaterno) + " " + str(self.amaterno)

class Catalogo(models.Model):
    nombre = models.CharField(max_length=50)
    tipoCatalogo = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    