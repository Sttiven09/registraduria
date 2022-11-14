from django.shortcuts import render, redirect
from consultaciudadanoApp.formularios.formCrearCiudadano import CiudadanoFrom
from django.contrib.auth.decorators import login_required

@login_required
def crearCiudadanos(request):
    
    if request.method == 'GET':
        return render(request,'crear_ciudadanos.html',{
            'form': CiudadanoFrom
    })
    else:
        try:

            form = CiudadanoFrom(request.POST)
            nuevoCiudadano = form.save(commit = False)
            nuevoCiudadano.user = request.user
            #print(nuevoCiudadano)
            nuevoCiudadano.save()
            return redirect('ciudadanos')
        except ValueError:
            return render(request,'crear_ciudadanos.html',{
            'form': CiudadanoFrom,
            'error': 'Digite toda la información'
    })