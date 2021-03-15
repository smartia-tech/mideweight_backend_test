from rest_framework import serializers

from .models import (Gateway,
                     GatewayTag,
                     GatewayStatus,
                     Posse)


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = "__all__"


# This acts as a base serializer for gateway, for internal use and doesn't work with any view
class BaseGatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = "__all__"


class GatewayTagSerializer(serializers.ModelSerializer):
    datasource = BaseGatewaySerializer(read_only=True)

    class Meta:
        model = GatewayTag
        fields = "__all__"


class GatewaySerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(read_only=True)
    queue_name = serializers.CharField(read_only=True)
    tags = GatewayTagSerializer(many=True, read_only=True)
    data_flow = serializers.BooleanField(read_only=True)

    class Meta:
        model = Gateway
        exclude = ['updated_at', 'created_at']

    """  
    Leaving this here because I saw a comment on validating client_id in the data_source.model.py
    file, It's a little bit vague so I'll be leaving that out.
    Ideally, any form of validation would be within this validate method
    def validate(self, attrs):
        pass
    """


class GatewayStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = GatewayStatus
        exclude = ['created_at']
