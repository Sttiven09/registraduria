from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def iniciarSesion(request):

    if request.method == 'GET':
        #print('enviado formulario')
        return render(request, 'iniciosesion.html',{
        'from': AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'iniciosesion.html',{
            'from': AuthenticationForm,
            'error': 'El usuario no se encuentra Registrado!!'
        })
        else:
            login(request, user)
            return redirect('bienvenida')
