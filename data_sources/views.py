from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from data_sources.models import Gateway, GatewayStatus, Posse
from data_sources.serializers import (
    GatewayReadSerializer,
    GatewayStatusSerializer,
    GatewayWriteSerializer,
    PosseSerializer,
)


class PossListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PosseSerializer
    queryset = Posse.objects.all()


class PossRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PosseSerializer
    queryset = Posse.objects.all()


class BaseGatewayAPIView:
    def get_serializer_class(self):
        if self.request.method == "GET":
            return GatewayReadSerializer
        else:
            return GatewayWriteSerializer


class GatewayListCreateAPIView(BaseGatewayAPIView, generics.ListCreateAPIView):
    """
       Endpoint to handle list and create API for Gateways
    """

    queryset = Gateway.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ("label", "posse", "serial_number", "location")
    ordering_fields = ("created_at", "updated_at")
    ordering = ("-updated_at",)


class GatewayRetrieveUpdateDestroyAPIView(
    BaseGatewayAPIView, generics.RetrieveUpdateDestroyAPIView
):
    """
        Endpoint to handle retrieve, update and destroy for Gateway instance
    """

    queryset = Gateway.objects.all()


class GatewayStatusListAPIView(generics.ListCreateAPIView):
    """
    This endpoint list the statuses for a gateway.
    """

    serializer_class = GatewayStatusSerializer
    queryset = GatewayStatus.objects.all()


class GatewayStatusRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint to retrieve, update and delete Gateway Status
    """
    serializer_class = GatewayStatusSerializer
    queryset = GatewayStatus.objects.all()

    def filter_queryset(self, queryset):
        queryset = super().get_queryset()
        gateway_id = self.kwargs.get("gateway_id")
        return queryset.filter(gateway_id=gateway_id)