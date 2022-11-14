from django.shortcuts import render
from consultaciudadanoApp.models import Ciudadanos
from django.contrib.auth.decorators import login_required

@login_required
def ciudadanos(request):
    ciudadanos = Ciudadanos.objects.all()

    return render(request, 'ciudadanos.html', {'ciudadanos': ciudadanos })
