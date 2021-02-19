from rest_framework import serializers

from data_sources.models import Posse, Gateway
from libs.utils import is_request_verbose


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = ('label', 'id',)


class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = '__all__'

    def to_representation(self, instance):
        if is_request_verbose(self.context.get('request')):
            self.fields['posse'] = PosseSerializer(read_only=True)
        return super(GatewaySerializer, self).to_representation(instance)
