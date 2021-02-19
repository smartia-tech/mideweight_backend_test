from rest_framework.viewsets import ModelViewSet

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag
from data_sources.serializers import PosseSerializer, GatewaySerializer, GatewayStatusSerializer, GatewayTagSerializer
from data_sources.permissions import HasAPIAccess
from libs.throttles import SmartiaRateLimit


class PosseView(ModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
    permission_classes = (HasAPIAccess,)
    throttle_classes = [SmartiaRateLimit]


class GatewayView(ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    permission_classes = (HasAPIAccess,)
    throttle_classes = [SmartiaRateLimit]

class GatewayStatusView(ModelViewSet):
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer
    permission_classes = (HasAPIAccess,)
    throttle_classes = [SmartiaRateLimit]


class GatewayTagView(ModelViewSet):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer
    permission_classes = (HasAPIAccess,)
    throttle_classes = [SmartiaRateLimit]
