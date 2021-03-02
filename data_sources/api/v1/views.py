from rest_framework import viewsets

from data_sources.models import Gateway
from data_sources.api.v1.serializers import (
    GatewaySerializer
)


class GatewayViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
