from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from data_sources.models import Posse, Gateway, GatewayTag, GatewayStatus
from data_sources.serializers import (
    PosseSerializer, GatewaySerializer, GatewayTagSerializer, GatewayStatusSerializer
)


class PosseView(ModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer


class GatewayView(ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer


class GatewayTagsView(ModelViewSet):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer


class GatewayStatusView(ModelViewSet):
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer
