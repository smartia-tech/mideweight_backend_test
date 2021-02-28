from rest_framework import serializers

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
