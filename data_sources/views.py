from rest_framework.viewsets import ModelViewSet

from data_sources.models import Posse, Gateway
from data_sources.serializers import PosseSerializer, GatewaySerializer
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
