from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag
from data_sources.serializers import PosseSerializer, GatewaySerializer, GatewayStatusSerializer, GatewayTagSerializer


class PosseViewSet(ModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
    filterset_fields = ('label', )


class GatewayViewSet(ModelViewSet):
    queryset = Gateway.objects.all().select_related('posse')
    serializer_class = GatewaySerializer
    filterset_fields = ('label', 'location', 'oauth2_client_id', 'serial_number', 'posse__label')


class GatewayStatusViewSet(ModelViewSet):
    queryset = GatewayStatus.objects.all().select_related('gateway')
    serializer_class = GatewayStatusSerializer
    filterset_fields = ('hostname', 'data_flow', 'os_name', 'os_version',
                        'firmware_version', 'maio_edge_version', 'gateway__label',
                        'gateway__location', 'gateway__oauth2_client_id', 'gateway__serial_number',
                        'gateway__posse__label')


class GatewayTagViewSet(ModelViewSet):
    queryset = GatewayTag.objects.all().select_related('gateway')
    serializer_class = GatewayTagSerializer
    filterset_fields = ('label', 'data_flow', 'hardware_name', 'unit_name',
                        'unit_type', 'status', 'gateway__label',
                        'gateway__location', 'gateway__oauth2_client_id', 'gateway__serial_number',
                        'gateway__posse__label')
