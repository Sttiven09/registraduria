from django.db import models
from .fuerza import Fuerza
from .rango import Rango


class Personalfp(models.Model):
    idpersonalfp = models.AutoField(primary_key=True)
    identificacion = models.IntegerField(default=0)
    nombres = models.TextField(max_length=100)
    apellidos = models.TextField(max_length=100)
    correoelectronico = models.TextField(max_length=60)
    id_fuerza  = models.ForeignKey(Fuerza,  on_delete = models.CASCADE)
    id_rango  = models.ForeignKey(Rango,  on_delete = models.CASCADE)

    def __str__(self):
        #return self.id_venta, self.cantidad
        return f'id: {self.idpersonalfp} identificacion: {self.identificacion}  nombres: {self.nombres} apellidos: {self.apellidos} correoelectrónico: {self.correoelectronico} fuerza: {self.id_fuerza} rango: {self.id_rango}'

