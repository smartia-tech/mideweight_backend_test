from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView
from data_sources.models import (
    Posse, Gateway,
    GatewayStatus, GatewayTag
)
from data_sources.serializers import (
    PosseSerializer, GatewaySerializer,
    GatewayStatusSerializer, GatewayTagSerializers
)


class PosseView(ListAPIView):
    '''
    Returns a paginated response(15 per page) of all `Posse` instances ordered by id, 
    this list can be filtered by labels through query parameters,
    you can also supply a specific page number you want to access

    **Examples

    .. code-block:: http

        GET  /api/posses/?search={label name}
    '''

    serializer_class = PosseSerializer
    queryset = Posse.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['label',]
    ordering_fields = ['label',]


class PosseDetailView(RetrieveAPIView):
    '''
    returns a detailed response for a specific Posse whose id is provided in the url, returns `404` if object is not found
    '''
    serializer_class = PosseSerializer
    queryset = Posse.objects.all()


class GatewayView(ListAPIView):
    '''
    Returns a paginated response(15 per page) of all `GateWay` instances ordered by id, 
    this list can be filtered by `labels, location or posse label` through query parameters,
    returns an `empty list` if filtered parameter not found
    you can also supply a specific page number you want to access

    **Examples

    .. code-block:: http

        GET  /api/gateways/?search={location}
    '''
    serializer_class = GatewaySerializer
    queryset = Gateway.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['label', 'location','posse__label']
    ordering_fields = ['label', 'location', 'posse__label']


class GatewayDetailView(RetrieveAPIView):
    '''
    returns a detailed response for a specific Gateway whose id is provided in the url, returns `404` if object is not found
    '''
    serializer_class = GatewaySerializer
    queryset = Gateway.objects.all()


class GatewayStatusView(ListAPIView):
    '''
    Returns a paginated response(15 per page) of all `GatewayStatus` instances ordered by id, 
    this list can be filtered by `hostname or os_name` through query parameters,
    returns an `empty list` if filtered parameter not found
    you can also supply a specific page number you want to access

    **Examples

    .. code-block:: http

        GET  /api/gateways/?search={os_name}
    '''
    serializer_class = GatewayStatusSerializer
    queryset = GatewayStatus.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['hostname', 'os_name']
    ordering_fields = ['hostname', 'os_name']




class GatewayStatusDetailView(RetrieveAPIView):
    '''
    returns a detailed response for a specific GatewayStatus whose id is provided in the url, returns `404` if object is not found
    '''
    serializer_class = GatewayStatusSerializer
    queryset = GatewayStatus.objects.all()


class GatewayTagView(ListAPIView):
    '''
    Returns a paginated response(15 per page) of all `GatewayTag` instances ordered by id, 
    this list can be filtered by `hardware_name, unit_name orstatus` through query parameters,
    returns an `empty list` if filtered parameter not found
    you can also supply a specific page number you want to access

    **Examples

    .. code-block:: http

        GET  /api/gateways/?search={location}
    '''
    serializer_class = GatewayTagSerializers
    queryset = GatewayTag.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['hardware_name', 'unit_name', 'status']
    ordering_fields = ['hardware_name', 'unit_name', 'status']
    


class GatewayTagDetailView(RetrieveAPIView):
    '''
    returns a detailed response for a specific GatewayTag whose id is provided in the url, returns `404` if object is not found
    '''
    serializer_class = GatewayTagSerializers
    queryset = GatewayTag.objects.all()
