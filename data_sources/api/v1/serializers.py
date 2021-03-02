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


class GatewaySerializer(serializers.ModelSerializer):
    """
    Post Serializer for Gateway Model
    """

    class Meta:
        model = Gateway
        fields = "__all__"


class GatewayGetSerializer(serializers.ModelSerializer):
    """
    Get Serializer for Gateway Model
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


class GatewayStatusSerializer(serializers.ModelSerializer):
    """
    Gateway status Post Serializer
    """

    class Meta:
        model = GatewayStatus
        fields = "__all__"


class GatewayStatusGetSerializer(serializers.ModelSerializer):
    """
    Gateway status Get Serializer
    """

    class Meta:
        model = GatewayStatus
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.upper() == 'GET':
            fields['gateway'] = GatewayGetSerializer(
                context=self.context,
                read_only=True
            )
        return fields


class GatewayTagSerializer(serializers.ModelSerializer):
    """
    Post serializer for GatewayTag
    """

    class Meta:
        model = GatewayTag
        fields = "__all__"

        extra_kwargs = {
            'unit_name': {
                'required': True,
                'allow_blank': False,
            }
        }


class GatewayTagGetSerializer(serializers.ModelSerializer):
    """
    Get serializer for GatewayTag 
    """

    datasource = serializers.SerializerMethodField()

    class Meta:
        model = GatewayTag
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.upper() == 'GET':
            fields['gateway'] = GatewayGetSerializer(
                context=self.context,
                read_only=True
            )
        return fields

    def get_datasource(self, obj):
        return obj.datasource
