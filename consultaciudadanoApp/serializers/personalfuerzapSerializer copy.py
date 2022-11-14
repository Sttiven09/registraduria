from rest_framework import serializers
from consultaciudadanoApp.models.personalfuerzap import Personalfp

class personalfpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalfp
        fields = [' idpersonalfp ','identificacion','nombres','apellidos','correoelectronico','id_fuerza','id_rango']