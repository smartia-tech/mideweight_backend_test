from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from data_sources.models import Gateway, GatewayStatus, Posse


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = ("id", "label")


class BaseGatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = (
            "id",
            "label",
            "posse",
            "location",
            "oauth2_client_id",
            "serial_number",
            "type_name",
            "queue_name",
            "tags",
            "data_flow",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("type_name",)
        validators = [
            UniqueTogetherValidator(
                queryset=Gateway.objects.all(), fields=["serial_number", "label"]
            )
        ]


class GatewayReadSerializer(BaseGatewaySerializer):
    """
    Serializer to handle read request on Gateway
    """

    posse = PosseSerializer()


class GatewayWriteSerializer(BaseGatewaySerializer):
    """
    Serializer to handle write request
    """

    pass


class GatewayStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatewayStatus
        fields = (
            "gateway",
            "hostname",
            "data_flow",
            "os_name",
            "os_version",
            "firmware_version",
            "maio_edge_version",
            "created_at",
        )

