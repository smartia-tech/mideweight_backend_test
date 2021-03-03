__author__ = 'Sunday Alexander'
from rest_framework import serializers
# import model class
from data_sources.models import Posse, Gateway, GatewayTag, GatewayStatus

"""
POSSE SERIALIZER BEGINS HERE..
"""


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = "__all__"


"""
GATEWAY SERIALIZER BEGINS HERE..
"""


class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = "__all__"


class GatewayGetSerializer(serializers.ModelSerializer):
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


"""
GATEWAY STATUS SERIALIZER BEGINS HERE..
"""


class GatewayStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatewayStatus
        fields = "__all__"


class GatewayStatusGetSerializer(serializers.ModelSerializer):
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


"""
GATEWAY TAG SERIALIZER BEGINS HERE..
"""


class GatewayTagSerializer(serializers.ModelSerializer):
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
