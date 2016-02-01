from django.db import models

class Usuario(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    telefono = models.CharField(max_length=16)

    def __unicode__(self):
        return self.cedula


class Provincia(models.Model):
    codigo = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=32)

    def __unicode__(self):
        return self.nombre

    
class Ciudad(models.Model):
    codigo = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=32)
    cod_prov = models.ForeignKey(Provincia)

    def __unicode__(self):
        return self.nombre

class Direccion(models.Model):
    principal = models.CharField(max_length=64)
    secundaria = models.CharField(max_length=64)
    referencia = models.CharField(max_length=128)
    cod_usuario = models.ForeignKey(Usuario)
    cod_prov = models.ForeignKey(Provincia)
    cod_city = models.ForeignKey(Ciudad)

class Transaccion(models.Model):
    n_transferencia = models.IntegerField(unique=True)
    f_pago = models.DateField()
    imagen = models.ImageField(upload_to = 'documentos_pago',  verbose_name='Imagen')
