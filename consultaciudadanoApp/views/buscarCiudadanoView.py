from django.shortcuts import render, get_object_or_404
from consultaciudadanoApp.models import Ciudadanos
from django.contrib.auth.decorators import login_required


@login_required
def buscarCiudadano(request ):
    if request.method == 'GET':
        
        return render(request, 'buscarCiudadano.html')
    else:
        if request.POST['identificacion1'] == request.POST['identificacion2']:
        
                id_ciudadano = request.POST.get("identificacion1")
                #print(id_ciudadano)
                ciudadano = Ciudadanos.objects.get(identificacion= id_ciudadano)
                ciudadano = get_object_or_404(Ciudadanos, identificacion= id_ciudadano)
                
                return render(request,'mostrar_ciudadano.html', {'ciudadano': ciudadano})
                
        else:
                return render(request, 'buscarCiudadano.html',{
                    
                    "error": 'Los documentos digitados no son iguales'
                })     