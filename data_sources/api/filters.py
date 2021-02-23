from django_filters import rest_framework as filters

from data_sources.models import Posse, Gateway, GatewayTag


class PosseFilter(filters.FilterSet):
    label = filters.CharFilter(lookup_expr='icontains')


class GatewayFilter(PosseFilter):
    location = filters.CharFilter(lookup_expr='icontains')
    serial_number = filters.CharFilter(lookup_expr='icontains')
    oauth2_client_id = filters.CharFilter(lookup_expr='icontains')
    posse = filters.ModelChoiceFilter(queryset=Posse.objects.all())


class GatewayStatusFilter(filters.FilterSet):
    hostname = filters.CharFilter(lookup_expr='icontains')
    data_flow = filters.BooleanFilter()
    os_name = filters.CharFilter(lookup_expr='icontains')
    os_version = filters.CharFilter(lookup_expr='icontains')
    firmware_version = filters.CharFilter(lookup_expr='icontains')
    maio_edge_version = filters.CharFilter(lookup_expr='icontains')
    created_at = filters.IsoDateTimeFilter()
    gateway = filters.ModelChoiceFilter(queryset=Gateway.objects.all())


class GatewayTagFilter(PosseFilter):
    created_at = filters.IsoDateTimeFilter()
    updated_at = filters.IsoDateTimeFilter()
    data_flow = filters.BooleanFilter()
    hardware_name = filters.CharFilter(lookup_expr='icontains')
    unit_name = filters.CharFilter(lookup_expr='icontains')
    unit_type = filters.ChoiceFilter(choices=GatewayTag.UNIT_TYPES)
    status = filters.ChoiceFilter(choices=GatewayTag.STATUSES)
    gateway = filters.ModelChoiceFilter(queryset=Gateway.objects.all())
