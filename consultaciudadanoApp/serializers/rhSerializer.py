from rest_framework import serializers
from consultaciudadanoApp.models.rh import Tiposangre

class tiposangreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiposangre
        fields = [' id_rh ','tipo_rh']