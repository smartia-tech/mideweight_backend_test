from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from data_sources.api.v1.serializers import (
    GatewayGetSerializer, GatewaySerializer,
    PosseSerializer, GatewayTagSerializer,
    GatewayTagGetSerializer, GatewayStatusSerializer,
    GatewayStatusGetSerializer
)
from data_sources.models import (
    Gateway, GatewayTag, Posse, GatewayStatus
)


class PosseViewSet(viewsets.ModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['label']


class GatewayViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewayGetSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = [
        'label',
        'posse__label',
        'location',
        'oauth2_client_id',
        'serial_number',
        'type_name'
    ]
    filter_fields = [
        'posse',
    ]

    ordering_fields = [
        'created_at',
        'updated_at'
    ]

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action.lower() in ['post', 'put']:
            serializer = GatewaySerializer
        return serializer


class GatewayTagViewSet(viewsets.ModelViewSet):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagGetSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = [
        'gateway__label',
        'hardware_name',
        'unit_name',
    ]
    filter_fields = [
        'gateway',
        'unit_type',
        'status',
        'data_flow'
    ]

    ordering_fields = [
        'created_at',
        'updated_at'
    ]

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action.lower() in ['post', 'put']:
            serializer = GatewayTagSerializer
        return serializer


class GatewayStatusViewSet(viewsets.ModelViewSet):
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusGetSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = [
        'gateway__label',
        'hostname',
        'os_name',
        'firmware_version',
        'maio_edge_version',
    ]
    filter_fields = [
        'gateway',
        'data_flow'
    ]

    ordering_fields = [
        'created_at',
    ]

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action.lower() in ['post', 'put']:
            serializer = GatewayStatusSerializer
        return serializer
