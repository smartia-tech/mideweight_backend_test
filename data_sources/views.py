from rest_framework import viewsets

from data_sources.serializers import (
    PosseSerializer,
    GatewaySerializer,
    GatewayStatusSerializer,
    GatewayTagSerializer,
    )
from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


class PosseViewSet(viewsets.ModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer


class GatewayViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    filterset_fields = ("label", "serial_number", "oauth2_client_id")


class GatewayStatusViewSet(viewsets.ModelViewSet):
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer
    filterset_fields = ("os_version",)


class GatewayTagViewSet(viewsets.ModelViewSet):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer
    filterset_fields = ("hardware_name", "gateway_id")
