from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from data_sources.models import Gateway, GatewayStatus, GatewayTag, Posse


class PosseSerializer(serializers.ModelSerializer):

	class Meta:
		model = Posse
		fields = '__all__'


class GatewayTagSerializer(serializers.ModelSerializer):

	class Meta:
		model = GatewayTag
		fields = '__all__'
		extra_kwargs = {'gateway': {"write_only": True}}

		validators = [
			UniqueTogetherValidator(
				queryset=GatewayTag.objects.all(),
				fields=('gateway', 'hardware_name')
			),
			UniqueTogetherValidator(
				queryset=GatewayTag.objects.all(),
				fields=('gateway', 'label')
			),

		]


class GatewayStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = GatewayStatus
		fields = '__all__'
		extra_kwargs = {'gateway': {"write_only": True}}


class GatewaySerializer(serializers.ModelSerializer):
	queue_name = serializers.CharField(read_only=True)
	data_flow = serializers.BooleanField(read_only=True)
	tags = GatewayTagSerializer(many=True, read_only=True)
	status = GatewayStatusSerializer(many=True, read_only=True)

	class Meta:
		model = Gateway
		fields = '__all__'

		validators = [
			UniqueTogetherValidator(
				queryset=Gateway.objects.all(),
				fields=('label', 'serial_number')
			),
		]

	def to_representation(self, instance):
		self.fields['posse'] = PosseSerializer(read_only=True)
		return super(GatewaySerializer, self).to_representation(instance)

