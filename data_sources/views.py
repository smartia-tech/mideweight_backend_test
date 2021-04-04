from django.shortcuts import render
from rest_framework import generics
from .models import Posse, Gateway, GatewayTag, GatewayStatus
from .serializers import PosseSerializer, GatewaySerializer, GatewayTagSerializer, GatewayStatusSerializer
from rest_framework.renderers import BrowsableAPIRenderer
from utils.renderer import CustomRenderer
from rest_framework import filters


# Create your views here.

class PosseApiView(generics.ListCreateAPIView):
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    # filter_backends = (filters.SearchFilter, )
    filter_fields = []
    ordering_fields = []
    search_fields = ("label", )
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer


class PosseDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer


class GatewayApiView(generics.ListCreateAPIView):
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    search_fields = ['label']
    filter_backends = (filters.SearchFilter,)


class GatewayDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    search_fields = ("label", )


class GatewayTagApiView(generics.ListCreateAPIView):
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer
    filter_backends = (filters.SearchFilter, )
    filter_fields = []
    ordering_fields = []
    search_fields = ("hardware_name", "unit_name")


class GatewayTagDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer


class GatewayStatusApiView(generics.ListCreateAPIView):
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer
    filter_backends = (filters.SearchFilter, )
    filter_fields = []
    ordering_fields = []
    search_fields = ("host_name", "os_name")


class GatewayStatusDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer

