from rest_framework import serializers
from .models import Posse, GatewayStatus, Gateway, GatewayTag
from rest_framework.validators import UniqueTogetherValidator


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = "__all__"


class GatewaySerializer(serializers.ModelSerializer):
    posse = serializers.PrimaryKeyRelatedField(queryset=Posse.objects.all())

    class Meta:
        model = Gateway
        fields = "__all__"


class GatewayTagSerializer(serializers.ModelSerializer):
    unit_type = serializers.ChoiceField(choices=["bool", "float", "str", "int"])
    status = serializers.ChoiceField(choices=["active", "disabled", "dormant"])
    gateway = serializers.PrimaryKeyRelatedField(queryset=Gateway.objects.all())

    class Meta:
        model = GatewayTag
        fields = "__all__"

        validators = [UniqueTogetherValidator(
            queryset=GatewayTag.objects.all(),
            fields=('gateway', 'hardware_name')
        )
        ]


class GatewayStatusSerializer(serializers.ModelSerializer):
    gateway = serializers.PrimaryKeyRelatedField(queryset=Gateway.objects.all(), write_only=True)

    class Meta:
        model = GatewayStatus
        fields = "__all__"

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['hostname'] < 3:
            raise serializers.ValidationError(detail={"hostname": "length of host_name must be greater 2"})
        return data
