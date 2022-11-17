from django.contrib import admin
from django.urls import path, include

from consultaciudadanoApp.urls import router_ciudadanos
from consultaciudadanoApp.views import pagPrincipalView
from consultaciudadanoApp.views import registro
from consultaciudadanoApp.views import mostrarCiudadanosView
from consultaciudadanoApp.views import pagCerrarSesionView
from consultaciudadanoApp.views import inicioSesionView
from consultaciudadanoApp.views import crearCiudadanosView
#from consultaciudadanoApp.views import actualizarCiudadanoView
from consultaciudadanoApp.views import buscarCiudadanoView
from consultaciudadanoApp.views import bienvenidaView
from consultaciudadanoApp.views import consultarUsuario
from consultaciudadanoApp.views import generarPDF
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', pagPrincipalView.principal, name = "index"),
    path('bienvenida/', bienvenidaView.bienvenida, name = "bienvenida"),
    path('ciudadanos/', mostrarCiudadanosView.ciudadanos, name = "ciudadanos"),
    path('ciudadanos/crear/', crearCiudadanosView.crearCiudadanos, name = "crear_ciudadanos"),
    #path('ciudadanos/actualizar/<int:id_ciudadano>', actualizarCiudadanoView.actualizarCiudadanos, name = "actualizar_ciudadanos"),
    #path('ciudadanos/<int:id_ciudadano>/', mostrarCiudadanoView.mostrarCiudadanos, name = "mostrar_ciudadanos"),
    path('ciudadanos/buscar/', buscarCiudadanoView.buscarCiudadano, name = "ciudadanos_buscar"),
    path('buscar/Usuario/', consultarUsuario.buscarusuario, name = "ciudadanos_buscarusuario"),
    #ath('ciudadanos/generar/pdf/', generarListaView , name = "generar_pdf"),
    path('registro/', registro.ingresar, name = "registro"),
    path('iniciarsesion/',inicioSesionView.iniciarSesion , name = "iniciarsesion"),
    path('cerrarsesion/',pagCerrarSesionView.cerrar , name = "cerrarsesion"),
    path('generarpdf/',generarPDF.generarPDF.as_view() , name = "generarpdf"),

    path('buscar/Usuario/cambiocontraseña/', auth_views.PasswordResetView.as_view(template_name="ingresarcorreo.html"), name = "password_reset"),
    path('mensaje/cambiocontraseña/',auth_views.PasswordResetDoneView.as_view(template_name="mensajeEnviocorreo.html") , name = "password_reset_done"),
    path('cambio/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="formcontraseña.html"), name = "password_reset_confirm"),
    path('cambio/verificado/', auth_views.PasswordResetCompleteView.as_view(template_name="cambioContraseña.html"), name = "password_reset_complete"),
    
    path('api/', include(router_ciudadanos.urls)),
]
