# DRF Imports
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
# Model Imports
from rest_framework.viewsets import ModelViewSet

from data_sources.models import *
from data_sources.serializers import GatewaySerializer, PosseSerializer, DataSourceBaseSerializer, \
    AbstractTagSerializer, \
    GatewayStatusSerializer, GatewayTagSerializer


# Gateway View Section
class ClientGatewayApiView(APIView):
    # TODO: Add authentication
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_client_gateway_object(self, client_id=None, **kwargs):
        """ Retrieve Gateway with client_id.
            In this case we assume that client_id is unique,
            and that one client_id  can connect to multiple gateways"""
        # Retrieve kwargs
        if kwargs:
            filter_dict = {k: v for k, v in kwargs}
            if client_id:
                try:
                    return Gateway.objects.filter(client_id=client_id, **filter_dict)
                except Gateway.DoesNotExist as gateway_error:
                    # Add Method to post debug info to DB here
                    return None, str(gateway_error.message)
            else:
                return None
        else:
            try:
                return Gateway.objects.filter(client_id=client_id), ''
            except Gateway.DoesNotExist as gateway_error:
                return None, gateway_error

    def get(self, request, client_id=None, **kwargs):
        # Define the Gateway Instance
        if client_id and kwargs:
            client_gateway_instance = self.get_client_gateway_object(oauth2_client_id=client_id, **kwargs)
        elif kwargs:
            client_gateway_instance = self.get_client_gateway_object(**kwargs)
        else:
            client_gateway_instance = None
        if not client_gateway_instance:
            return Response(
                {"res": "No Gateway object with matching client id exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = GatewaySerializer(client_gateway_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, client_id=None, **kwargs):
        """Update The Client Gateway Object with given client_id"""
        client_gateway_instance = self.get_client_gateway_object(client_id=client_id)

        if not client_gateway_instance:
            return Response(
                {"res": "Gateway Object with specified Paramaters does not Exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'label': request.data.get('label'),
            'posse': request.data.get('posse'),
            'location': request.data.get('location'),
            'serial_number': request.data.get('serial_number'),
            'type_name': request.data.get('type_name')
        }

        serializer = GatewaySerializer(client_gateway_instance, data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class GatewayApiView(APIView):
    # TODO: Add Authentication
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_gateway_object(self, **kwargs):
        """Retrieve ALL Gateway Object Data from Model"""
        if not kwargs:
            try:
                gateway_object = Gateway.objects.all()
                return gateway_object, ''
            except Gateway.DoesNotExist as gateway_error:
                return None, gateway_error.message
        else:
            filter_dict = {k: v for k, v in kwargs}
            try:
                gateway_object = Gateway.objects.filter(**filter_dict)
                return gateway_object, ''
            except Gateway.DoesNotExist as gateway_error:
                return None, gateway_error.message

    def get(self, request, **kwargs):

        if kwargs:
            gateway_instance = self.get_gateway_object(kwargs=kwargs)
        else:
            gateway_instance = self.get_gateway_object()

        if not gateway_instance:
            return Response(
                {"res": "Gateway Object with specified Paramaters does not Exist"},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = GatewaySerializer(gateway_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):

        if kwargs:
            gateway_instance, gateway_error = self.get_gateway_object(kwargs=kwargs)
        else:
            gateway_instance, gateway_error = self.get_gateway_object()

        if not gateway_instance:
            return Response(
                {"res": "Gateway Object with specified Paramaters does not Exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'label': request.data.get('label'),
            'posse': request.data.get('posse'),
            'location': request.data.get('location'),
            'serial_number': request.data.get('serial_number'),
            'type_name': request.data.get('type_name')
        }

        serializer = GatewaySerializer(gateway_instance, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Post Gateway Data"""
        data = {
            'label': request.data.get('label'),
            'posse': request.data.get('posse'),
            'location': request.data.get('location'),
            'serial_number': request.data.get('serial_number'),
            'type_name': request.data.get('type_name')
        }
        serializer = GatewaySerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# End of Gateway view Section

# Start -- Gateway Status View Section

# Only View Gateway Status'
# As it can be assumed that statusses are updated automatically,
# It should not be able to be edited via the API
class GatewayStatusApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_gateway_status_object(self, **kwargs):

        if kwargs:
            filter_dict = {k: v for k, v in kwargs}
            try:
                gateway_status_object = GatewayStatus.objects.filter(**filter_dict)
                return gateway_status_object, ''
            except GatewayStatus.DoesNotExist as gateway_status_error:
                return None, gateway_status_error
        else:
            try:
                gateway_status_object = GatewayStatus.objects.all()
                return gateway_status_object, ''
            except Gateway.DoesNotExist as gateway_status_error:
                return None, gateway_status_error.message

    def get(self, request, **kwargs):

        if kwargs:
            gateway_status_instance, gateway_status_error = self.get_gateway_status_object(kwargs=kwargs)
        else:
            gateway_status_instance, gateway_status_error = self.get_gateway_status_object()

        if not gateway_status_instance:
            return Response(
                {"res": "Gateway Status Object with specified Parameters does not Exist"},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = GatewayStatusSerializer(gateway_status_instance)

        if not serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


# End -- Gateway Status View Section

# Start Tag View Section
# A more simplistic approach with DRF ModelViewSet

class GatewayTagAPIView(ModelViewSet):
    # Fetch data from the database
    queryset = GatewayTag.objects.all()
    serializer = GatewayTagSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = [field.name for field in GatewayTag._meta.fields]
