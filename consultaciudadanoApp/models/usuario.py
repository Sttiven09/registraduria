from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from .fuerza import Fuerza
from .rango import Rango


#definir usuarios y superUsuarios
#class UsuarioManager(BaseUserManager):
#    def create_user(self, identificacion, email, username, nombres, apellidos,id_fuerza,id_rango, password=None):
#        if not email:
#            raise ValueError('El usuario no digito un correo')
#        usuario = self.model(
#            username= username,
#            identificacion=identificacion, 
#            email = self.normalize_email(email),
#            nombres= nombres,
#            apellidos= apellidos,
#            id_fuerza = id_fuerza,
#            id_rango = id_rango
#        )

#       usuario.set_password(password)
#        usuario.save()
#        return usuario

#    def create_superuser(self, identificacion, email, username, nombres, apellidos,id_fuerza,id_rango, password):
#        usuario = self.create_user(
#           username= username,
#            identificacion=identificacion, 
#            email=self.normalize_email(email),
#            nombres= nombres,
#            apellidos= apellidos,
#            id_fuerza = id_fuerza,
#            id_rango = id_rango
#        )
#        usuario.usuario_administrador = True
#        UsuarioNue.save()
#        return usuario


class usuario(AbstractBaseUser):
    usermane = models.CharField('Usuario',unique=True, max_length=100) 
    identificacion = models.IntegerField('Identificacion',unique=True)
    email= models.EmailField('Correo Electronico', max_length=100, unique= True)
    nombres = models.CharField('Nombres',max_length=150, blank=True, null= True)
    apellidos = models.CharField('Apellidos',max_length=150, blank=True, null= True)
    id_fuerza  = models.ForeignKey(Fuerza,  on_delete = models.CASCADE)
    id_rango  = models.ForeignKey(Rango,  on_delete = models.CASCADE)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [usermane, identificacion]



