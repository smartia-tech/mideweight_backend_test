from rest_framework import serializers

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
    gateway_id = serializers.CharField(write_only=True, source='gateway')

    class Meta:
        model = GatewayTag
        exclude = ('gateway',)
