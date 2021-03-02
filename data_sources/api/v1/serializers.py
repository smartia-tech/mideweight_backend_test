from rest_framework import serializers

from data_sources.models import (
    Posse,
    Gateway,
    GatewayTag,
    GatewayStatus
)


class PosseSerializer(serializers.ModelSerializer):
    """
    Serializer for Posse Model
    """

    class Meta:
        model = Posse
        fields = "__all__"


class GatewayTagSerializer(serializers.ModelSerializer):
    """
    serializer for GatewayTag instances
    """

    datasource = serializers.SerializerMethodField()

    class Meta:
        model = GatewayTag
        fields = "__all__"

    def get_datasource(self, obj):
        return obj.datasource


class GatewaySerializer(serializers.ModelSerializer):
    """
    Serializer for Gateway Model
    """

    class Meta:
        model = Gateway
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.upper() == 'GET':
            fields['posse'] = PosseSerializer(
                context=self.context,
                read_only=True
            )
        return fields
