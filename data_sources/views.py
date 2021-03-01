from rest_framework import generics

from .models import Posse, Gateway, GatewayStatus, GatewayTag
from .serializers import PosseSerializer, GatewaySerializer, GatewayStatusSerializer, GatewayTagSerializer


class PosseList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing posse.

    post:
    Create a new posse instance.
    """
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer


class PosseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return a specific posse instance.

    put:
    Update the the specific posse instance.

    patch:
    Partial update the specific posse instance.

    delete:
    Delete the the specific posse instance.
    """
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer


class GatewayList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing gateway.

    post:
    Create a new gateway instance.
    """
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer


class GatewayDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return a specific gateway instance.

    put:
    Update the the specific gateway instance.

    patch:
    Partial update the specific gateway instance.

    delete:
    Delete the the specific gateway instance.
    """
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer


class GatewayStatusList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing gateway status.

    post:
    Create a new gateway status instance.
    """
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer


class GatewayStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return a specific gateway status instance.

    put:
    Update the the specific gateway status instance.

    patch:
    Partial update the specific gateway status instance.

    delete:
    Delete the the specific gateway status instance.
    """
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer


class GatewayTagList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing gateway tag.

    post:
    Create a new gateway tag instance.
    """
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer


class GatewayTagDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return a specific gateway tag instance.

    put:
    Update the the specific gateway tag instance.

    patch:
    Partial update the specific gateway tag instance.

    delete:
    Delete the the specific gateway tag instance.
    """
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer
