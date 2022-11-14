from rest_framework import serializers
from consultaciudadanoApp.models.estado import Estado

class estadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id_estado','estado','descricion']