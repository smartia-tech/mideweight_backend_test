from rest_framework import serializers
from django.core import serializers as django_serializers
from .models import Posse, Gateway, GatewayStatus, GatewayTag

class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = ['label']

class GatewaySerializer(serializers.ModelSerializer):
    posse = serializers.PrimaryKeyRelatedField(queryset=Posse.objects.all())
    class Meta:
        model = Gateway
        fields = ['label', 'location', 'serial_number', 'type_name', 'posse', 'queue_name', 'data_flow']

class GatewayStatusSerializer(serializers.ModelSerializer):
    gateway = serializers.PrimaryKeyRelatedField(queryset=Gateway.objects.all())
    class Meta:
        model = GatewayStatus
        fields = [
            'gateway',
            'hostname',
            'data_flow',
            'os_name',
            'os_version',
            'firmware_version',
            'maio_edge_version'
            ]

class GatewayTagSerializer(serializers.ModelSerializer):
    gateway = serializers.PrimaryKeyRelatedField(queryset=Gateway.objects.all())
    class Meta:
        model = GatewayTag
        fields = [
            'gateway',
            'data_flow',
            'hardware_name',
            'unit_name',
            'unit_type',
            'data_flow',
            'status',
            'label'
            ]
