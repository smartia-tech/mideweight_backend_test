# Import DRF
from rest_framework import serializers
# Import Models from data_sources
from data_sources.models import GatewayTag, AbstractTag, Posse, DataSourceBaseModel, Gateway, GatewayStatus


class AbstractTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractTag
        fields = ["label"]


class GatewayTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatewayTag
        fields = ["gateway", "data_flow", "hardware_name", "unit_name", "unit_type", "status"]


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = ["label"]


class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ["label", "posse", "location", "oauth2_client_id",
                  "serial_number", "type_name", ]


class DataSourceBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSourceBaseModel
        fields = ["label", "created_at", "updated_at", ]


class GatewayStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatewayStatus

        fields = ["gateway", "hostname", "data_flow", "os_name", "os_version",
                  "firmware_version", "maio_edge_version", "created_at"]
