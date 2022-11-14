from django.shortcuts import render, redirect, get_object_or_404
from consultaciudadanoApp.models import Ciudadanos
from consultaciudadanoApp.formularios import formCrearCiudadano
from django.contrib.auth.decorators import login_required

@login_required
def actualizarCiudadanos(request , id_ciudadano ):
    
    if request.method == 'GET':
        #ciudadano = Ciudadanos.objects.get(pk= id_ciudadano)
        ciudadano = get_object_or_404(Ciudadanos, pk= id_ciudadano)
        form = formCrearCiudadano(instance= ciudadano)
        return render(request,'mostrar_ciudadano.html', {'ciudadano': ciudadano})
    else:
        try:
            #ciudadano = Ciudadanos.objects.get(pk= id_ciudadano)
            ciudadano = get_object_or_404(Ciudadanos, pk= id_ciudadano, user=request.user)
            form = formCrearCiudadano(request.POST, instance= ciudadano)
            form.save()
            redirect('ciudadanos')
        except:
            return render(request,'mostrar_ciudadano.html', {'ciudadano': ciudadano, 'form': form,
            'error': 'error al actualizar la tarea'
            })