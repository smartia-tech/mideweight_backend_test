from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError
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
    search_fields = ('gateway__label', 'hostname', 'os_name',)


class GatewayTagView(ModelViewSet):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer
    permission_classes = (HasAPIAccess,)
    throttle_classes = [SmartiaRateLimit]
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('gateway__label', 'label', 'hardware_name')

    def get_queryset(self):
        unit_type = self.request.GET.get('unit_type')
        status_type = self.request.GET.get('status')
        self.validate_filter_value(unit_type, GatewayTag.UNIT_TYPES, 'unit type')
        self.validate_filter_value(status_type, GatewayTag.STATUSES, 'status')
        filter_fields = {}
        if unit_type:
            filter_fields['unit_type'] = unit_type
        if status_type:
            filter_fields['status'] = status_type
        return GatewayTag.objects.filter(**filter_fields)

    def validate_filter_value(self, value, choices, label):
        if value:
            formatted_choices = [choice[0] for choice in choices]
            if not value in formatted_choices:
                raise ValidationError("{} has to be one of {}".format(label, formatted_choices))
