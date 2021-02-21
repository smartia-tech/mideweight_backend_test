from django.shortcuts import render
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
    serializer_class = PosseSerializer
    queryset = Posse.objects.all()


class PosseDetailView(RetrieveAPIView):
    serializer_class = PosseSerializer
    queryset = Posse.objects.all()


class GatewayView(ListAPIView):
    serializer_class = GatewaySerializer
    queryset = Gateway.objects.all()


class GatewayDetailView(RetrieveAPIView):
    serializer_class = GatewaySerializer
    queryset = Gateway.objects.all()


class GatewayStatusView(ListAPIView):
    serializer_class = GatewayStatusSerializer
    queryset = GatewayStatus.objects.all()


class GatewayStatusDetailView(RetrieveAPIView):
    serializer_class = GatewayStatusSerializer
    queryset = GatewayStatus.objects.all()


class GatewayTagView(ListAPIView):
    serializer_class = GatewayTagSerializers
    queryset = GatewayTag.objects.all()


class GatewayTagDetailView(RetrieveAPIView):
    serializer_class = GatewayTagSerializers
    queryset = GatewayTag.objects.all()
