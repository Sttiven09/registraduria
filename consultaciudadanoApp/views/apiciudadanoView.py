from rest_framework.viewsets import ModelViewSet

from consultaciudadanoApp.models import Ciudadanos
from consultaciudadanoApp.serializers import ciudadanosSerializer

class ciudadanosAPIviewSet(ModelViewSet):
    serializer_class = ciudadanosSerializer
    queryset = Ciudadanos.objects.all()