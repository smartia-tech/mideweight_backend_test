from rest_framework import serializers
from .models import Posse, Gateway, GatewayStatus, GatewayTag


class PosseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posse
        fields = "__all__"


class GatewaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gateway
        fields = "__all__"


class GatewayStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = GatewayStatus
        fields = "__all__"


class GatewayTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = GatewayTag
        fields = "__all__"