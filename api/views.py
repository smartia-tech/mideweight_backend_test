from rest_framework.viewsets import ModelViewSet


from api.serializers import (PosseSerializer, GatewaySerializer,
                             GatewayStatusSerializer, GatewayTagSerializer)
from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


class PosseView(ModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer


class GatewayView(ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer


class GatewayStatusView(ModelViewSet):
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer


class GatewayTagView(ModelViewSet):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer
