from rest_framework import viewsets

from data_sources.api.v1.serializers import (
    GatewayGetSerializer,
    GatewaySerializer,
    PosseSerializer
)
from data_sources.models import Gateway, Posse


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
