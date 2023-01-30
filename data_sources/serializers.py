from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from data_sources.models import Gateway, GatewayStatus, GatewayTag, Posse


class PosseSerializer(ModelSerializer):
    class Meta:
        model = Posse
        fields = '__all__'


class GatewayTagSerializer(ModelSerializer):
    class Meta:
        model = GatewayTag
        fields = '__all__'
        validators = (
            UniqueTogetherValidator(
                queryset=GatewayTag.objects.all(),
                fields=('gateway', 'label'),
                message='Uniqueness Breached: gateway and label should be'
                'unique in GatewayTag.',
            ),
            UniqueTogetherValidator(
                queryset=GatewayTag.objects.all(),
                fields=('gateway', 'hardware_name'),
                message='Uniqueness Breached: gateway and hardware_name'
                'should be unique in GatewayTag.',
            ),
        )


class GatewaySerializer(ModelSerializer):
    tags = GatewayTagSerializer(many=True, read_only=True)

    class Meta:
        model = Gateway
        fields = (
            'id',
            'created_at',
            'updated_at',
            'label',
            'location',
            'oauth2_client_id',
            'serial_number',
            'posse',
            'queue_name',
            'data_flow',
            'tags',
        )
        read_only_fields = ('queue_name', 'data_flow', 'tags')
        validators = (UniqueTogetherValidator(
            queryset=Gateway.objects.all(),
            fields=('label', 'serial_number'),
            message='Uniqueness Breached: label and serial number should be'
            'unique in Gateway.',
        ), )


class GatewayStatusSerializer(ModelSerializer):
    class Meta:
        model = GatewayStatus
        fields = '__all__'
