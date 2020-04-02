from rest_framework import routers, serializers, viewsets

from Profile.models import modeloProfile
from Profile.models import modeloCiudad
from Profile.models import modeloGenero
from Profile.models import modeloOcupacion
from Profile.models import modeloEstado
from Profile.models import modeloEstadoCivil

class EstadoCivilSerializers(serializers.ModelSerializer):
    class Meta:
        model = modeloEstadoCivil
        fields = ('__all__')

class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = modeloEstado
        fields = ('__all__')

class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = modeloOcupacion
        fields = ('__all__')

class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = modeloGenero
        fields = ('__all__')

class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = modeloCiudad
        fields = ('__all__')

class Profile1Serializers(serializers.ModelSerializer):
    class Meta:
        model = modeloProfile
        # fields = ('nombre', 'apellidoPaterno','apellidoMaterno', 'edad')
        fields = ('__all__')
