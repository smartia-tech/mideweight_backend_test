from .models import Posse, Gateway, GatewayStatus, GatewayTag
from . import serializers
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class PosseView(viewsets.ModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = serializers.PosseSerializer

class GatewayViewSet(viewsets.ModelViewSet):
    model = Gateway
    queryset = model.objects.all()
    serializer_class = serializers.GatewaySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = [field.name for field in model._meta.fields]

class GatewayStatusViewSet(viewsets.ModelViewSet):
    model = GatewayStatus
    queryset = model.objects.all()
    serializer_class = serializers.GatewayStatusSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = [field.name for field in model._meta.fields]

class GatewayTagViewSet(viewsets.ModelViewSet):
    model = GatewayTag
    queryset = model.objects.all()
    serializer_class = serializers.GatewayTagSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = [field.name for field in model._meta.fields]


