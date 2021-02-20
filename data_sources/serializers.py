from rest_framework import serializers

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag
from libs.utils import is_request_verbose


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = ('label', 'id',)


class BaseGatewayStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatewayStatus
        fields = '__all__'


class BaseGatewayTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatewayTag
        fields = '__all__'


class BaseGatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = '__all__'


class ReferenceGatewayStatusSerializer(BaseGatewayStatusSerializer):
    # showing gateway in status object for a verbose request in /gateway is unnecessary.
    # It would only use more resources
    class Meta:
        model = GatewayStatus
        exclude = ('gateway',)


class ReferenceGatewayTagSerializer(BaseGatewayTagSerializer):
    # showing gateway in tags object for a verbose request in /gateway is unnecessary.
    # It would only use more resources
    class Meta:
        model = GatewayTag
        exclude = ('gateway',)


class ReferenceBaseGatewaySerializer(BaseGatewaySerializer):
    pass


class GatewaySerializer(BaseGatewaySerializer):
    tags = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    status = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    def to_representation(self, instance):
        if is_request_verbose(self.context.get('request')):
            self.fields['posse'] = PosseSerializer(read_only=True)
            self.fields['status'] = ReferenceGatewayStatusSerializer(read_only=True, many=True)
            self.fields['tags'] = ReferenceGatewayTagSerializer(read_only=True, many=True)
        return super(GatewaySerializer, self).to_representation(instance)


class GatewayStatusSerializer(BaseGatewayStatusSerializer):
    def to_representation(self, instance):
        if is_request_verbose(self.context.get('request')):
            self.fields['gateway'] = ReferenceBaseGatewaySerializer(read_only=True)
        return super(GatewayStatusSerializer, self).to_representation(instance)


class GatewayTagSerializer(BaseGatewayTagSerializer):
    def to_representation(self, instance):
        if is_request_verbose(self.context.get('request')):
            self.fields['gateway'] = ReferenceBaseGatewaySerializer(read_only=True)
        return super(GatewayTagSerializer, self).to_representation(instance)
