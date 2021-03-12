from rest_framework import status
from rest_framework import generics

from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend

from drf_yasg.utils import swagger_auto_schema

from .serializers import GatewaySerializer, GatewayStatusSerializer, GatewayTagSerializer, PosseSerializer
from .models import Posse, Gateway, GatewayStatus, GatewayTag

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="description from swagger_auto_schema via method_decorator"
))
class PosseView(generics.ListCreateAPIView):
    
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['label']

class PosseDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
    


class GatewayView(generics.ListCreateAPIView):

    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['label', 'posse', 'oauth2_client_id']


class GatewayDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer

class GatewayStatusView(generics.ListCreateAPIView):

    queryset = GatewayStatus.objects.all()
    serializer_class = GatewaySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['os_name', 'hostname']


class GatewayStatusDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = GatewayStatus.objects.all()
    serializer_class = GatewaySerializer


class GatewayTagView(generics.ListCreateAPIView):

    queryset = GatewayTag.objects.all()
    serializer_class = GatewaySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['unit_type', 'unit_name', 'status']


class GatewayTagDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = GatewayTag.objects.all()
    serializer_class = GatewaySerializer
