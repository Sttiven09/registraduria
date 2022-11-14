from django.db import models

class Tiposangre(models.Model):
    id_rh = models.AutoField(primary_key=True)
    tipo_rh = models.TextField(max_length=10)

    def __str__(self):
        #return self.id_venta, self.cantidad
        return f'{self.tipo_rh}'
