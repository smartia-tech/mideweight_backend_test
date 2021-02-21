from rest_framework import serializers
from data_sources.models import (
    Posse, Gateway,
    GatewayStatus, GatewayTag
)


class PosseSerializer(serializers.ModelSerializer):
    '''
    serializer for Posse instances
    '''

    class Meta:
        model = Posse
        fields = "__all__"




class GatewayTagSerializers(serializers.ModelSerializer):
    '''
    serializer for GatewayTag instances
    '''
    datasource = serializers.CharField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = GatewayTag
        fields = ('__all__')
    
    def get_created_at(self, obj: GatewayTag) -> str:
        '''
        format the returned created time, make it more readable
        '''
        time = obj.created_at
        formated_time = time.strftime("%Y-%m-%d %H:%M:%S")
        return formated_time
    
    def get_updated_at(self, obj: GatewayTag) -> str:
        '''
        format the returned updated time, make it more readable
        '''
        time = obj.updated_at
        formated_time = time.strftime("%Y-%m-%d %H:%M:%S")
        return formated_time


class GatewaySerializer(serializers.ModelSerializer):
    '''
    serializer for Gateway instances
    '''
    data_flow = serializers.BooleanField()
    queue_name = serializers.CharField()
    tags = GatewayTagSerializers(many=True, read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Gateway
        fields = "__all__"
    
    def get_created_at(self, obj: Gateway) -> str:
        '''
        format the returned created time, make it more readable
        '''
        time = obj.created_at
        formated_time = time.strftime("%Y-%m-%d %H:%M:%S")
        return formated_time
    
    def get_updated_at(self, obj: Gateway) -> str:
        '''
        format the returned updated time, make it more readable
        '''
        time = obj.updated_at
        formated_time = time.strftime("%Y-%m-%d %H:%M:%S")
        return formated_time


class GatewayStatusSerializer(serializers.ModelSerializer):
    '''
    serializer for GatewayStatus instances
    '''
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = GatewayStatus
        fields = ('__all__')
    
    def get_created_at(self, obj: GatewayStatus) -> str:
        '''
        format the returned created time, make it more readable
        '''
        time = obj.created_at
        formated_time = time.strftime("%Y-%m-%d %H:%M:%S")
        return formated_time
    
    def get_updated_at(self, obj: GatewayStatus) -> str:
        '''
        format the returned updated time, make it more readable
        '''
        time = obj.updated_at
        formated_time = time.strftime("%Y-%m-%d %H:%M:%S")
        return formated_time
