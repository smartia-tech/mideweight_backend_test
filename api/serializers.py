from rest_framework import serializers

from data_sources.models import (
    Gateway,
    GatewayStatus,
    GatewayTag,
    Posse,
)


class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = '__all__'


class GatewayStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatewayStatus
        fields = '__all__'


class GatewayTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatewayTag
        fields = '__all__'


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = '__all__'
