from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.reverse import reverse

from data_sources.models import Gateway, GatewayStatus, GatewayTag, Posse
from data_sources.serializers import (GatewaySerializer,
                                      GatewayStatusSerializer,
                                      GatewayTagSerializer, PosseSerializer)


class PosseList(ListCreateAPIView):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer

    @staticmethod
    def url():
        return reverse('data_sources:posse_list')


class PosseDetail(RetrieveUpdateDestroyAPIView):  #pylint: disable=too-many-ancestors
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer

    @staticmethod
    def url(pk: int):
        return reverse('data_sources:posse_detail', kwargs={'pk': pk})


class GatewayList(ListCreateAPIView):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer

    @staticmethod
    def url():
        return reverse('data_sources:gateway_list')


class GatewayDetail(RetrieveUpdateDestroyAPIView):  #pylint: disable=too-many-ancestors
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer

    @staticmethod
    def url(pk: int):
        return reverse('data_sources:gateway_detail', kwargs={'pk': pk})


class GatewayStatusList(ListCreateAPIView):
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer

    @staticmethod
    def url():
        return reverse('data_sources:gateway_status_list')


class GatewayStatusDetail(RetrieveUpdateDestroyAPIView):  #pylint: disable=too-many-ancestors
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer

    @staticmethod
    def url(pk: int):
        return reverse('data_sources:gateway_status_detail', kwargs={'pk': pk})


class GatewayTagList(ListCreateAPIView):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer

    @staticmethod
    def url():
        return reverse('data_sources:gateway_tag_list')


class GatewayTagDetail(RetrieveUpdateDestroyAPIView):  #pylint: disable=too-many-ancestors
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer

    @staticmethod
    def url(pk: int):
        return reverse('data_sources:gateway_tag_detail', kwargs={'pk': pk})
