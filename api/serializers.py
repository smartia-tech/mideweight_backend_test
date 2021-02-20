from rest_framework import serializers

from data_sources.models import Posse


class PosseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posse
        fields = '__all__'
