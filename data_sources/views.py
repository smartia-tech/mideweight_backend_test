from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag
from data_sources.serializers import PosseSerializer, GatewaySerializer, GatewayStatusSerializer, GatewayTagSerializer
from data_sources.permissions import HasAPIAccess
from libs.throttles import SmartiaRateLimit


class PosseView(ModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
    permission_classes = (HasAPIAccess,)
    throttle_classes = [SmartiaRateLimit]
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('label',)


class GatewayView(ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    permission_classes = (HasAPIAccess,)
    throttle_classes = [SmartiaRateLimit]
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('label', 'posse__label', 'location', 'serial_number')


class GatewayStatusView(ModelViewSet):
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer
    permission_classes = (HasAPIAccess,)
    throttle_classes = [SmartiaRateLimit]
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('gateway__label', 'label', 'hostname', 'os_name',)


class GatewayTagView(ModelViewSet):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer
    permission_classes = (HasAPIAccess,)
    throttle_classes = [SmartiaRateLimit]
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('gateway__label', 'label', 'hardware_name')
