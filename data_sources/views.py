from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import (
    Posse, Gateway, GatewayStatus, GatewayTag
)
from .serializers import (
    PosseSerializer, GatewayStatusSerializer, GatewaySerializer,
    GatewayTagSerializer
)


class PosseView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        posse_all = Posse.objects.all()
        serializer = PosseSerializer(posse_all, many=True)
        return Response(serializer.data)


class GatewayView(APIView):
    permission_class = [AllowAny]

    def get(self, request):
        gateway_all = Gateway.objects.all()
        serializer = GatewaySerializer(gateway_all, many=True)
        return Response(serializer.data)


class GatewayStatusView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        getway_status = GatewayStatus.objects.all()
        serializer = GatewayStatusSerializer(getway_status, many=True)
        return Response(serializer.data)


class GatewayTagView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        getway_tag = GatewayTag.objects.all()
        serializer = GatewayTagSerializer(getway_tag, many=True)
        return Response(serializer.data)
