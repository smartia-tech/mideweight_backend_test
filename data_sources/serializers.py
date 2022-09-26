from rest_framework import serializers
from data_sources.models import Gateway, GatewayStatus, GatewayTag, Posse


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = ('id', 'label')


class GatewaySerializer(serializers.ModelSerializer):
    posse = PosseSerializer(read_only=True)
    posse_id = serializers.PrimaryKeyRelatedField(
        queryset=Posse.objects.all(), source='posse', write_only=True)

    class Meta:
        model = Gateway
        fields = ('id', 'posse', 'label', 'posse_id', 'location', 'oauth2_client_id', 'serial_number', 'type_name',
                  'queue_name', 'data_flow', 'tags', 'created_at', 'updated_at')


class GatewayStatusSerializer(serializers.ModelSerializer):
    gateway = GatewaySerializer(read_only=True)
    gateway_id = serializers.PrimaryKeyRelatedField(
        queryset=Gateway.objects.all(), source='gateway', write_only=True)

    class Meta:
        model = GatewayStatus
        fields = ('id', 'gateway', 'gateway_id', 'hostname', 'data_flow', 'os_name', 'os_version', 'firmware_version',
                  'maio_edge_version', 'created_at')


class GatewayTagSerializer(serializers.ModelSerializer):
    gateway = GatewaySerializer(read_only=True)
    gateway_id = serializers.PrimaryKeyRelatedField(
        queryset=Gateway.objects.all(), source='gateway', write_only=True)

    class Meta:
        model = GatewayTag
        fields = ('id', 'label', 'gateway', 'gateway_id', 'data_flow', 'hardware_name', 'unit_name', 'unit_type',
                  'status', 'datasource')
