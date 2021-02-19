from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Gateway
from .serializers import GatewaySerializer


class GatewaysView(ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
