from rest_framework import serializers
from .models import Posse, Gateway, GatewayStatus, GatewayTag

class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = ['label']

class GatewaySerializer(serializers.ModelSerializer):
    posse_label = serializers.CharField(source='posse.label')

    class Meta:
        model = Gateway
        fields = ['label', 'posse_label', 'location', 'oauth2_client_id',
        'serial_number', 'created_at', 'updated_at', 'type_name']
    

class GatewayStatusSerializer(serializers.ModelSerializer):
    gateway_label = serializers.CharField(source='gateway.label')
    gateway_posse_label = serializers.CharField(source='gateway.posse.label')
    gateway_location = serializers.CharField(source='gateway.location')
    gateway_oauth2_client_id = serializers.CharField(source='gateway.oauth2_client_id')
    gateway_serial_number = serializers.CharField(source='gateway.serial_number')
    gateway_created_at = serializers.DateTimeField(source='gateway.created_at')
    gateway_updated_at = serializers.DateTimeField(source='gateway.updated_at')
    gateway_type_name = serializers.CharField(source='gateway.type_name')

    class Meta:
        model = GatewayStatus
        fields = ['gateway_label', 'gateway_posse_label', 'gateway_location',
        'gateway_oauth2_client_id', 'gateway_serial_number', 'gateway_created_at',
        'gateway_updated_at', 'gateway_type_name', 'hostname', 'data_flow', 
        'os_name', 'os_version', 'firmware_version', 'maio_edge_version',
        'created_at']


class GatewayTagSerializer(serializers.ModelSerializer):
    gateway_label = serializers.CharField(source='gateway.label')
    gateway_posse_label = serializers.CharField(source='gateway.posse.label')
    gateway_location = serializers.CharField(source='gateway.location')
    gateway_oauth2_client_id = serializers.CharField(source='gateway.oauth2_client_id')
    gateway_serial_number = serializers.CharField(source='gateway.serial_number')
    gateway_created_at = serializers.DateTimeField(source='gateway.created_at')
    gateway_updated_at = serializers.DateTimeField(source='gateway.updated_at')
    gateway_type_name = serializers.CharField(source='gateway.type_name')

    class Meta:
        model = GatewayTag
        fields = ['gateway_label', 'gateway_posse_label', 'gateway_location',
        'gateway_oauth2_client_id', 'gateway_serial_number', 'gateway_created_at',
        'gateway_updated_at', 'gateway_type_name', 'data_flow', 'hardware_name',
        'unit_name', 'unit_type', 'status', 'label', 'created_at', 'updated_at']   