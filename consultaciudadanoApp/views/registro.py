from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

@login_required



def ingresar(request):

    if request.method == 'GET':
        #print('enviado formulario')
        return render(request, 'registro.html',{
            'from': UserCreationForm
    })
    else:
        #print('obteniendo datos')
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'], email=request.POST['email'], first_name = request.POST['first_name'], last_name = request.POST['last_name'])
                user.save()
                login(request, user)
                return redirect('bienvenida')
                #return HttpResponse('usuario creado satisfactoriamente')
            except IntegrityError:
                return render(request, 'registro.html',{
                    'from': UserCreationForm,
                    "error": 'el usuario ya existe'
                })

        return render(request, 'registro.html',{
                    'from': UserCreationForm,
                    "error": 'las contraseñas no son iguales'
                }) 
        

