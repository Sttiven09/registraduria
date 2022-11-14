from django.db import models

class Estado(models.Model):
    id_estado= models.AutoField(primary_key=True)
    estado = models.TextField(max_length=50)
    descricion = models.TextField(max_length=100)

    def __str__(self):
        #return self.id_venta, self.cantidad
        #return f'id: {self.id_estado} Estado Ciudadano:{self.estado} descripcion: {self.descricion}'
        return f'{self.estado}'
        
        