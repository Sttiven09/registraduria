from django.db import models

from .rh import Tiposangre
from .estado import Estado
from django.contrib.auth.models import User

class Ciudadanos(models.Model):
    idciudadano = models.AutoField(primary_key=True)
    identificacion = models.IntegerField(unique= True)
    nombres = models.TextField(max_length=100)
    apellidos = models.TextField(max_length=100)
    fechadenacimiento = models.DateField()
    lugardenacimiento = models.TextField(max_length=50)
    fechadeexpedicion = models.DateField()
    lugardeexpedicion = models.TextField(max_length=50)
    estatura = models.IntegerField()
    id_rh = models.ForeignKey(Tiposangre, null=True, on_delete = models.CASCADE)
    id_estado  = models.ForeignKey(Estado,  null=True, on_delete = models.CASCADE)
    usuario = models.ForeignKey(User, null=True, on_delete = models.CASCADE)


    def __str__(self):
        #return self.id_venta, self.cantidad
        return f'id: {self.idciudadano} identificacion: {self.identificacion}  nombres: {self.nombres} id: {self.id_estado}'
        
