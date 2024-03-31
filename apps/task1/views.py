from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView

from apps.task1.serializers import MyTokenObtainPairSerializer


class MyCustomObtainTokenView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
