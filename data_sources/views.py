from rest_framework.viewsets import ModelViewSet

from data_sources.models import Posse
from data_sources.serializers import PosseSerializer
from data_sources.permissions import HasAPIAccess
from libs.throttles import SmartiaRateLimit


class PosseView(ModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
    permission_classes = (HasAPIAccess,)
    throttle_classes = [SmartiaRateLimit]
