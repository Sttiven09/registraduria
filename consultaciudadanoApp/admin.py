from django.contrib import admin
from .models.ciudadanos import Ciudadanos
from .models.rh import Tiposangre
from .models.estado import Estado
#from .models.personalfuerzap import Personalfp
from .models.fuerza import Fuerza
from .models.rango import Rango

# Register your models here.
@admin.register(Ciudadanos)
class adminCiudadanos(admin.ModelAdmin):
    list_display = ('idciudadano','identificacion','nombres','apellidos')
    list_display_links = ('nombres',)
    list_filter = ('id_estado',)
    list_per_page = 10
@admin.register(Estado)
class adminEstados(admin.ModelAdmin):
    list_display = ('id_estado','estado','descricion')
    #exclude =('id_estado','estado','descricion') no permite editar
@admin.register(Tiposangre)
class adminTiposangre(admin.ModelAdmin):
    list_display = ('id_rh','tipo_rh')
#@admin.register(Personalfp)
#class adminPersonalfuerzapublica(admin.ModelAdmin):
#    list_display = ('idpersonalfp','identificacion','nombres','apellidos','apellidos','correoelectronico',)
#    list_display_links = ('nombres',)
#    list_filter = ('id_fuerza',)
#    list_per_page = 10
@admin.register(Fuerza)
class adminFuerza(admin.ModelAdmin):
    list_display = ('id_fuerza','fuerzapublica')
@admin.register(Rango)
class adminRango(admin.ModelAdmin):
    list_display = ('id_fuerza','fuerzapublica')
    ordering =('id_fuerza',)
    
    

#admin.site.register(Ciudadanos,Administrador)
#admin.site.register(Tiposangre,Administrador)
#admin.site.register(Estado,Administrador)
#admin.site.register(Personalfp,Administrador)
#admin.site.register(Fuerza,Administrador)
#admin.site.register(Rango,Administrador)

#admin.site.register(Ciudadanos)
#admin.site.register(Tiposangre)
#admin.site.register(Estado)
#admin.site.register(Personalfp)
#admin.site.register(Fuerza)
#admin.site.register(Rango)
