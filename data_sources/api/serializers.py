from rest_framework import serializers, validators

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = ('id', 'label', )


class GatewaySerializer(serializers.ModelSerializer):
    posse = PosseSerializer(read_only=True)
    posse_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Gateway
        fields = (
            'id',
            'label',
            'created_at',
            'updated_at',
            'posse',
            'posse_id',
            'type_name',
            'location',
            'oauth2_client_id',
            'serial_number',
            'queue_name',
            'tags',
            'data_flow',
        )
        read_only = (
            'type_name',
            )
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Gateway.objects.all(),
                fields=['label', 'serial_number']
            ),
        ]


class GatewayStatusSerializer(serializers.ModelSerializer):
    gateway = GatewaySerializer(read_only=True)
    gateway_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = GatewayStatus
        fields = (
            'id',
            'hostname',
            'data_flow',
            'os_name',
            'os_version',
            'firmware_version',
            'maio_edge_version',
            'created_at',
            'gateway',
            'gateway_id',
        )


class GatewayTagSerializer(serializers.ModelSerializer):
    gateway = GatewaySerializer(read_only=True)
    gateway_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = GatewayTag
        fields = (
            'id',
            'label',
            'created_at',
            'updated_at',
            'data_flow',
            'hardware_name',
            'unit_name',
            'unit_type',
            'status',
            'gateway',
            'gateway_id',
        )
        validators = [
            validators.UniqueTogetherValidator(
                queryset=GatewayTag.objects.all(),
                fields=['gateway_id', 'label']
            ),
            validators.UniqueTogetherValidator(
                queryset=GatewayTag.objects.all(),
                fields=['gateway_id', 'hardware_name']
            )
        ]
