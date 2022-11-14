from rest_framework.routers import DefaultRouter
from consultaciudadanoApp.views.apiciudadanoView import ciudadanosAPIviewSet

router_ciudadanos = DefaultRouter()

router_ciudadanos.register(prefix='ciudadanos', basename='ciudadanos', viewset = ciudadanosAPIviewSet)