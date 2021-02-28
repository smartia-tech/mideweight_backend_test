from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = "__all__"


class GatewaySerializer(serializers.ModelSerializer):
    posse = PosseSerializer(read_only=True)
    posse_id = serializers.IntegerField(write_only=True)
    data_flow = serializers.BooleanField(read_only=True)
    queue_name = serializers.CharField(read_only=True)

    class Meta:
        model = Gateway
        fields = "__all__"
        read_only = ("type_name",)
        validators = (
            UniqueTogetherValidator(
                queryset=Gateway.objects.all(),
                fields=('label', 'serial_number'),
                message='Label and serial number must be unique',
            ),
        )


class GatewayStatusSerializer(serializers.ModelSerializer):
    gateway = GatewaySerializer(read_only=True)
    gateway_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = GatewayStatus
        fields = "__all__"


class GatewayTagSerializer(serializers.ModelSerializer):
    gateway = GatewaySerializer(read_only=True)
    gateway_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = GatewayTag
        fields = "__all__"
        validators = (
            UniqueTogetherValidator(
                queryset=GatewayTag.objects.all(),
                fields=('gateway_id', 'label'),
                message='Gateway_id and label must be unique'
            ),
            UniqueTogetherValidator(
                queryset=GatewayTag.objects.all(),
                fields=('gateway_id', 'hardware_name'),
                message='Gateway_id and hardware_name must be unique'
            ),
        )
