from rest_framework import serializers
from consultaciudadanoApp.models.rango import Rango

class rangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rango
        fields = [' id_fuerza ','fuerzapublica']