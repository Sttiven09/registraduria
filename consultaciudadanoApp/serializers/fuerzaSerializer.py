from rest_framework import serializers
from consultaciudadanoApp.models.fuerza import Fuerza

class fuerzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuerza
        fields = [' id_fuerza ','fuerzapublica']