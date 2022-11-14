from django.db import models

class Fuerza(models.Model):
    id_fuerza= models.AutoField(primary_key=True)
    fuerzapublica = models.TextField(max_length=100)

    def __str__(self):
        #return self.id_venta, self.cantidad
        return f'Fuerza Publica:{self.fuerzapublica}'
