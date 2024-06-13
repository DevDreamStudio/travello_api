from django.shortcuts import render

from rest_framework import generics
from . import serializers, models


class SimpleUserCreateAPIView(generics.CreateAPIView):
    queryset = models.CustomSimpleUser.objects.all()
    serializer_class = serializers.SimpleCustomUserRegisterSerializer


class SimpleUserUpdateEmailAPIView(generics.UpdateAPIView):
    pass
