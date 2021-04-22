from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import userLoginSerializer,userRegisterSerializer

from .models import userLogin,userRegister

class userLoginViewSet(viewsets.ModelViewSet):
    queryset = userLogin.objects.all().order_by('name')
    serializer_class = userLoginSerializer

class userRegisterViewSet(viewsets.ModelViewSet):
    queryset = userRegister.objects.all().order_by('email')
    serializer_class = userRegisterSerializer





