from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from data_sources.models import (
    Gateway,
    GatewayStatus,
    GatewayTag,
    Posse,
)

from .serializers import (
    GatewaySerializer,
    GatewayStatusSerializer,
    GatewayTagSerializer,
    PosseSerializer,
)


class GatewayViewSet(viewsets.ModelViewSet):
    serializer_class = GatewaySerializer
    queryset = Gateway.objects.all()

    @action(detail=True)
    def tags(self, request, pk=None):
        gateway = self.get_object()
        tags = [
            GatewayTagSerializer(tag).data
            for tag in gateway.tags
        ]

        if len(tags):
            return Response(tags, status=status.HTTP_200_OK)
        else:
            return Response(
                {"detail": f"No tags found for Gateway with ID ({pk})"},
                status=status.HTTP_404_NOT_FOUND,
            )

    @action(detail=True)
    def dataflow(self, request, pk=None):
        gateway = self.get_object()
        return Response({"data_flow": gateway.data_flow})


class GatewayStatusViewSet(viewsets.ModelViewSet):
    serializer_class = GatewayStatusSerializer
    queryset = GatewayStatus.objects.all()


class GatewayTagViewSet(viewsets.ModelViewSet):
    serializer_class = GatewayTagSerializer
    queryset = GatewayTag.objects.all()


class PosseViewSet(viewsets.ModelViewSet):
    serializer_class = PosseSerializer
    queryset = Posse.objects.all()
