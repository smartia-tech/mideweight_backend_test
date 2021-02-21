from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters

from data_sources.models import Gateway, Posse, GatewayStatus, GatewayTag
from data_sources.serializers import GatewaySerializer, PosseSerializer, GatewayStatusSerializer, GatewayTagSerializer


class GatewayViewSet(viewsets.ModelViewSet):
    """Gateway viewsets"""

    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    permission_classes = []
    http_method_names = ['post', 'get', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['label', 'location', 'serial_number', 'posse__label']
    filter_fields = ['location', 'label']
    ordering_fields = ['created_at']


class PosseViewSet(viewsets.ModelViewSet):
    """Posse viewsets"""

    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
    permission_classes = []
    http_method_names = ['post', 'get', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['label', ]
    filter_fields = ['label']
    ordering_fields = ['created_at']


class GatewayStatusViewSet(viewsets.ModelViewSet):
    """Gateway Status viewsets"""

    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer
    permission_classes = []
    http_method_names = ['post', 'get', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['os_name', 'os_version', 'firmware_version', 'gateway__label']
    filter_fields = ['os_name', 'os_version', 'firmware_version', 'maio_edge_version', 'hostname']
    ordering_fields = ['created_at']


class GatewayTagViewSet(viewsets.ModelViewSet):
    """Gateway Tag viewsets"""

    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer
    permission_classes = []
    http_method_names = ['post', 'get', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['status', 'unit_name', 'hardware_name', 'gateway__label', 'unit_type']
    filter_fields = ['status', 'unit_name', 'hardware_name', 'gateway__label', 'unit_type']
    ordering_fields = ['created_at', 'status']
