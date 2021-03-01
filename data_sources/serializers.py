from .models import Posse, Gateway, GatewayStatus, GatewayTag
from rest_framework import serializers


class PosseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Posse
		fields = ('label')


class GatewaySerializer(serializers.ModelSerializer):
	posse_id = serializers.PrimaryKeyRelatedField(source='posse', queryset=Posse.objects.all())
	posse = PosseSerializer(read_only=True)

	class Meta:
		model = Gateway
		fields = ('label', 'posse_id', 'posse', 'location', 'oauth2_client_id', 'serial_number', 'type_name', 'data_flow', 'tags', 'queue_name')

class GatewayStatusSerializer(serializers.ModelSerializer):
	gateway_id = serializers.PrimaryKeyRelatedField(source='gateway', queryset=Gateway.objects.all())
	gateway = GatewaySerializer(read_only=True)

	class Meta:
		model = GatewayStatus
		fields = ('gateway_id', 'gateway', 'hostname', 'data_flow', 'os_name', 'os_version', 'firmware_version', 'maio_edge_version','created_at')

class GatewayTagSerializer(serializers.ModelSerializer):
	gateway_id = serializers.PrimaryKeyRelatedField(source='gateway', queryset=Gateway.objects.all())
	gateway = GatewaySerializer(read_only=True)

	class Meta:
		model = GatewayStatus
		fields = ('label', 'gateway_id', 'gateway', 'data_flow', 'hardware_name', 'unit_name', 'unit_type', 'status', 'datasource')
		extra_kwargs = {
			'unit_name': {
				# Tell DRF that the link field is not required.
				'required': False,
				'allow_blank': True,
			}
		}
