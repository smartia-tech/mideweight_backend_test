from rest_framework import viewsets

from data_sources.api.serializers import (
    PosseSerializer,
    GatewaySerializer,
    GatewayStatusSerializer,
    GatewayTagSerializer,
    )
from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag
from data_sources.api.filters import (
    PosseFilter,
    GatewayFilter,
    GatewayStatusFilter,
    GatewayTagFilter,
    )


class PosseViewSet(viewsets.ModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
    filterset_class = PosseFilter


class GatewayViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    filterset_class = GatewayFilter


class GatewayStatusViewSet(viewsets.ModelViewSet):
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer
    filterset_class = GatewayStatusFilter


class GatewayTagViewSet(viewsets.ModelViewSet):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer
    filterset_class = GatewayTagFilter
