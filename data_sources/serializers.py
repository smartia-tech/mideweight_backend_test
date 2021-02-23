from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


class PosseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Posse
        fields = ('id', 'label')


class GatewaySerializer(FlexFieldsModelSerializer):
    expandable_fields = {'posse': PosseSerializer}

    class Meta:
        model = Gateway
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('serial_number', 'label'),
                message="serial_number and label "
                        "should be unique in Gateway."
            )]


class GatewayStatusSerializer(FlexFieldsModelSerializer):
    expandable_fields = {'gateway': GatewaySerializer}

    class Meta:
        model = GatewayStatus
        fields = '__all__'


class GatewayTagSerializer(FlexFieldsModelSerializer):
    expandable_fields = {'gateway': GatewaySerializer}

    class Meta:
        model = GatewayTag
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('gateway', 'label'),
                message="gateway and label "
                        "should be unique in GatewayTag."
            ),
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('gateway', 'hardware_name'),
                message="gateway and hardware_name "
                        "should be unique in GatewayTag."
            )
        ]
