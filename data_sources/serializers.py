from rest_framework import serializers

from .models import Posse, Gateway, GatewayStatus, GatewayTag


class PosseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posse
        fields = "__all__"


class GatewaySerializer(serializers.ModelSerializer):
    tags = GatewayTagSerialzer(many=True, read_only=True)
    data_flow = serializers.BooleanField()

    class Meta:
        model = Gateway
        fields = ('label', 'posse', 'location', 'serial_number', 'type_name', 'tags', 'data_flow')


class GatewayStatusSerializer(serializers.ModelSerializer):
    gateway = serializers.HypelinkedRelatedField(
        many=False,
        read_only=True,
        view_name='gateway'
    )

    class Meta:
        model = GatewayStatus
        fields = '__all__'


# There must a hard way to abstract datasource serializing but
# for now I don't think it worth doing unless the project may add many tags
# and datasource each week or two if that's the case we may be able to do some dirty work
# with automatic code replacement or something like that    
class GatewayTagSerialzer(serializers.ModelSerializer):
    gateway = serializers.HypelinkedRelatedField(
        many=False,
        read_only=True,
        view_name='gateway'
    )

    class Meta:
        model = GatewayTag
        fields = "__all__"
