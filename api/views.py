from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from api.serializers import (PosseSerializer, GatewaySerializer,
                             GatewayStatusSerializer, GatewayTagSerializer)
from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


class PosseView(ModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
    search_fields = ('label',)
    ordering_fields = ['label']
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)


class GatewayView(ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    search_fields = ('label', 'posse__label', 'location', 'serial_number')
    ordering_fields = ['label', 'posse__label', 'created_at', 'updated_at']
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)


class GatewayStatusView(ModelViewSet):
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer
    ordering_fields = ['hostname', 'created_at']
    search_fields = ('gateway__label', 'hostname', 'os_name', 'data_flow',
                     'os_version', 'firmware_version', 'maio_edge_version')
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)


class GatewayTagView(ModelViewSet):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    ordering_fields = ['label']
    search_fields = ('gateway__label', 'label', 'hardware_name',
                     'unit_name', 'unit_type', 'status', 'data_flow')
