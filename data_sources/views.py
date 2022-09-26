from django.shortcuts import render
from data_sources.serializers import PosseSerializer, GatewaySerializer
from data_sources.serializers import GatewayStatusSerializer
from data_sources.serializers import GatewayTagSerializer
from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag
from rest_framework import viewsets, permissions, generics, filters

# Create your views here.


def index(request):
    return render(request, 'index.html')

def posse(request):
    return render(request, 'posse.html')

def gateway(request):
    return render(request, 'gateway.html')

def status(request):
    return render(request, 'status.html')

def tag(request):
    return render(request, 'tag.html')



class PosseViewList(generics.ListAPIView):
    serializer_class = PosseSerializer

    def get_queryset(self):

        queryset = Posse.objects.all()
        query_label = self.request.query_params.get('label', None)
        if query_label is not None:
            queryset = queryset.filter(label__exact=query_label)
        return queryset

class GatewayViewList(generics.ListAPIView):
    serializer_class = GatewaySerializer

    def get_queryset(self):

        queryset = Gateway.objects.all()
        query_label = self.request.query_params.get('label', None)
        query_posse = self.request.query_params.get('posse', None)
        query_location = self.request.query_params.get('location', None)
        query_client = self.request.query_params.get('client', None)
        query_serial = self.request.query_params.get('serial', None)
        query_created = self.request.query_params.get('created', None)
        query_updated = self.request.query_params.get('updated', None)
        query_type = self.request.query_params.get('type', None)

        if query_label is not None:
            queryset = queryset.filter(label__exact=query_label)
        if query_posse is not None:
            queryset = queryset.filter(posse__label__exact=query_posse)
        if query_location is not None:
            queryset = queryset.filter(location__exact=query_location)
        if query_client is not None:
            queryset = queryset.filter(oauth2_client_id__exact=query_client)
        if query_serial is not None:
            queryset = queryset.filter(serial_number__exact=query_serial)
        if query_created is not None:
            queryset = queryset.filter(created_at__exact=query_created)
        if query_updated is not None:
            queryset = queryset.filter(updated_at__exact=query_updated)
        if query_type is not None:
            queryset = queryset.filter(type_name__exact=query_type)

        return queryset


class GatewayStatusViewList(generics.ListAPIView):
    serializer_class = GatewayStatusSerializer

    def get_queryset(self):

        queryset = GatewayStatus.objects.all()

        query_label = self.request.query_params.get('label', None)
        query_posse = self.request.query_params.get('posse', None)
        query_location = self.request.query_params.get('location', None)
        query_client = self.request.query_params.get('client', None)
        query_serial = self.request.query_params.get('serial', None)
        query_created = self.request.query_params.get('created', None)
        query_updated = self.request.query_params.get('updated', None)
        query_type = self.request.query_params.get('type', None)
        query_host = self.request.query_params.get('host', None)
        query_flow = self.request.query_params.get('flow', None)
        query_osname = self.request.query_params.get('osname', None)
        query_osver = self.request.query_params.get('osver', None)
        query_firm = self.request.query_params.get('firm', None)
        query_maio = self.request.query_params.get('maio', None)
        query_createdat = self.request.query_params.get('createdat', None)

        if query_label is not None:
            queryset = queryset.filter(gateway__label__exact=query_label)
        if query_posse is not None:
            queryset = queryset.filter(gateway__posse__label__exact=query_posse)
        if query_location is not None:
            queryset = queryset.filter(gateway__location__exact=query_location)
        if query_client is not None:
            queryset = queryset.filter(gateway__oauth2_client_id__exact=query_client)
        if query_serial is not None:
            queryset = queryset.filter(gateway__serial_number__exact=query_serial)
        if query_created is not None:
            queryset = queryset.filter(gateway__created_at__exact=query_created)
        if query_updated is not None:
            queryset = queryset.filter(gateway__updated_at__exact=query_updated)
        if query_type is not None:
            queryset = queryset.filter(gateway__type_name__exact=query_type)
        if query_host is not None:
            queryset = queryset.filter(hostname__exact=query_host)
        if query_flow is not None:
            queryset = queryset.filter(data_flow__exact=query_flow)
        if query_osname is not None:
            queryset = queryset.filter(os_name__exact=query_osname)
        if query_osver is not None:
            queryset = queryset.filter(os_version__exact=query_osver)
        if query_firm is not None:
            queryset = queryset.filter(firmware_version__exact=query_firm)
        if query_maio is not None:
            queryset = queryset.filter(maio_edge_version__exact=query_maio)
        if query_createdat is not None:
            queryset = queryset.filter(created_at__exact=query_createdat)
            
        return queryset


class GatewayTagViewList(generics.ListAPIView):
    serializer_class = GatewayTagSerializer

    def get_queryset(self):

        queryset = GatewayTag.objects.all()

        query_label = self.request.query_params.get('label', None)
        query_posse = self.request.query_params.get('posse', None)
        query_location = self.request.query_params.get('location', None)
        query_client = self.request.query_params.get('client', None)
        query_serial = self.request.query_params.get('serial', None)
        query_created = self.request.query_params.get('created', None)
        query_updated = self.request.query_params.get('updated', None)
        query_type = self.request.query_params.get('type', None)
        query_flow = self.request.query_params.get('flow', None)
        query_hard = self.request.query_params.get('hard', None)
        query_uname = self.request.query_params.get('uname', None)
        query_utype = self.request.query_params.get('utype', None)
        query_status = self.request.query_params.get('status', None)
        query_label = self.request.query_params.get('label', None)
        query_createdat = self.request.query_params.get('createdat', None)
        query_updatedat = self.request.query_params.get('updatedat', None)


        if query_label is not None:
            queryset = queryset.filter(gateway__label__exact=query_label)
        if query_posse is not None:
            queryset = queryset.filter(gateway__posse__label__exact=query_posse)
        if query_location is not None:
            queryset = queryset.filter(gateway__location__exact=query_location)
        if query_client is not None:
            queryset = queryset.filter(gateway__oauth2_client_id__exact=query_client)
        if query_serial is not None:
            queryset = queryset.filter(gateway__serial_number__exact=query_serial)
        if query_created is not None:
            queryset = queryset.filter(gateway__created_at__exact=query_created)
        if query_updated is not None:
            queryset = queryset.filter(gateway__updated_at__exact=query_updated)
        if query_type is not None:
            queryset = queryset.filter(gateway__type_name__exact=query_type)
        if query_flow is not None:
            queryset = queryset.filter(data_flow__exact=query_flow)
        if query_hard is not None:
            queryset = queryset.filter(hardware_name__exact=query_hard)
        if query_uname is not None:
            queryset = queryset.filter(unit_name__exact=query_uname)
        if query_utype is not None:
            queryset = queryset.filter(unit_type__exact=query_utype)
        if query_status is not None:
            queryset = queryset.filter(status__exact=query_status)
        if query_label is not None:
            queryset = queryset.filter(label__exact=query_label)
        if query_createdat is not None:
            queryset = queryset.filter(created_at__exact=query_createdat)
        if query_updatedat is not None:
            queryset = queryset.filter(updated_at__exact=query_updatedat)

        return queryset