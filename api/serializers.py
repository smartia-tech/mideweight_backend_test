from rest_framework import serializers

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


class PosseSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="posse-detail")

    class Meta:
        model = Posse
        fields = '__all__'


class GatewaySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="gateway-detail")
    tags = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    status = serializers.HyperlinkedIdentityField(
        view_name="gatewaystatus-detail")

    class Meta:
        model = Gateway
        fields = '__all__'


class GatewayStatusSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="gatewaystatus-detail")
    gateway = serializers.HyperlinkedIdentityField(view_name="gateway-detail")

    class Meta:
        model = GatewayStatus
        fields = '__all__'


class GatewayTagSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="gatewaytag-detail")

    class Meta:
        model = GatewayTag
        fields = '__all__'
