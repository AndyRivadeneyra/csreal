from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
# from Profile.views import CustonAuthToken
from Profile import views

urlpatterns = [
    # re_path(r'Profile/$', CustonAuthToken.as_view()),
    re_path(r'estadoCivil_lista1/$',views.EstadoCivilList.as_view()),
    re_path(r'estado_lista1/$',views.EstadoList.as_view()),
    re_path(r'ocupacion_lista1/$',views.OcupacionList.as_view()),
    re_path(r'genero_lista1/$',views.GeneroList.as_view()),
    re_path(r'ciudad_lista1/$',views.CiudadList.as_view()),
    re_path(r'profile_lista1/$',views.ProfileList.as_view()),
    #re_path(r'example_detail2/(?P<id>\d+)/$',views.ExampleDetail2.as_view())
]