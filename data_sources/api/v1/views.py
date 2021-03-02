from rest_framework import viewsets

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


class GatewayViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewayGetSerializer

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action.lower() in ['post', 'put']:
            serializer = GatewaySerializer
        return serializer


class GatewayTagViewSet(viewsets.ModelViewSet):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagGetSerializer

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action.lower() in ['post', 'put']:
            serializer = GatewayTagSerializer
        return serializer


class GatewayStatusViewSet(viewsets.ModelViewSet):
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusGetSerializer

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action.lower() in ['post', 'put']:
            serializer = GatewayStatusSerializer
        return serializer
