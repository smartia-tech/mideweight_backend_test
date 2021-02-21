from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


class PosseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="posse-detail")

    class Meta:
        model = Posse
        fields = '__all__'


class GatewaySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="gateway-detail")
    tags = serializers.HyperlinkedIdentityField(
        read_only=True, many=True, view_name="gatewaytag-detail")
    queue_name = serializers.ReadOnlyField()
    data_flow = serializers.ReadOnlyField()
    posse_id = serializers.IntegerField(write_only=True)
    posse = PosseSerializer(read_only=True)

    class Meta:
        model = Gateway
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Gateway.objects.all(),
                fields=['label', 'serial_number']
            )
        ]


class GatewayStatusSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="gatewaystatus-detail")
    gateway_url = serializers.HyperlinkedIdentityField(
        view_name="gateway-detail")
    gateway_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = GatewayStatus
        exclude = ('gateway',)


class GatewayTagSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="gatewaytag-detail")
    gateway_url = serializers.HyperlinkedIdentityField(
        view_name="gateway-detail")
    gateway_id = serializers.CharField(write_only=True)

    class Meta:
        model = GatewayTag
        exclude = ('gateway',)
        validators = [
            UniqueTogetherValidator(
                queryset=GatewayTag.objects.all(),
                fields=['gateway', 'label']
            ),
            UniqueTogetherValidator(
                queryset=GatewayTag.objects.all(),
                fields=['gateway', 'hardware_name']
            )
        ]
