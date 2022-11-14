from django.forms import ModelForm
from consultaciudadanoApp.models import Ciudadanos

class CiudadanoFrom(ModelForm):
    class Meta:
        model = Ciudadanos
        fields = ['identificacion','nombres','apellidos','fechadenacimiento','lugardenacimiento','fechadeexpedicion','lugardeexpedicion','estatura','id_rh','id_estado']
