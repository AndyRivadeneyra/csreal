from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from Profile.models import modeloProfile
from Profile.serializer import Profile1Serializers

from Profile.models import modeloCiudad
from Profile.serializer import CiudadSerializers

from Profile.models import modeloGenero
from Profile.serializer import GeneroSerializers

from Profile.models import modeloOcupacion
from Profile.serializer import OcupacionSerializers

from Profile.models import modeloEstado
from Profile.serializer import EstadoSerializers

from Profile.models import modeloEstadoCivil
from Profile.serializer import EstadoCivilSerializers

class EstadoCivilList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = modeloEstadoCivil.objects.filter(delete=False)
        serializer = EstadoCivilSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):   
        serializer = EstadoCivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = modeloEstado.objects.filter(delete=False)
        serializer = EstadoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = modeloOcupacion.objects.filter(delete=False)
        serializer = OcupacionSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class GeneroList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = modeloGenero.objects.filter(delete=False)
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class CiudadList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = modeloCiudad.objects.filter(delete=False)
        serializer = CiudadSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = modeloProfile.objects.filter(delete=False)
        serializer = Profile1Serializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Profile1Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
