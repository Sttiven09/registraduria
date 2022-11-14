from rest_framework.serializers import ModelSerializer
from consultaciudadanoApp.models.ciudadanos import Ciudadanos

class ciudadanosSerializer(ModelSerializer):
    class Meta:
        model = Ciudadanos
        fields = ['idciudadano','identificacion', 'nombres', 'apellidos','fechadenacimiento','lugardenacimiento','fechadeexpedicion','lugardeexpedicion','estatura','id_rh ','id_estado']
        #fields = '__all__'

