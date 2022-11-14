from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def buscarusuario(request ):
    if request.method == 'GET':
        
        return render(request, 'buscarUsuario.html')
    else:
        if request.POST['username1'] == request.POST['username2']:
        
                id_usuario = request.POST.get("username1")
                #print(id_usuario)
                usuario = User.objects.get(username= id_usuario)
                usuario = get_object_or_404(User, username= id_usuario)
                
                return render(request,'ingresarcorreo.html', {'ciudadano': usuario})
                
        else:
                return render(request, 'buscarUsuario.html',{
                    
                    "error": 'Los documentos digitados no son iguales'
                })     
