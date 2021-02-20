from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from data_sources.serializers import PosseSerializer, GatewaySerializer, GatewayStatusSerializer,\
    ReferenceGatewayStatusSerializer, ReferenceBaseGatewaySerializer
from data_sources.models import Posse, Gateway, GatewayStatus


class TestPosse(TestCase):
    def setUp(self):
        self.url = '/api/v1/posse/'
        self.client = APIClient()

        Posse.objects.create(label='Posse Label 1')
        Posse.objects.create(label='Posse Label 2')

    def test_posse(self):
        response = self.client.get(path=self.url, HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        posses = Posse.objects.all()
        serializer = PosseSerializer(posses, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(path=self.url,
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx',
                                   data={'label': 'Holla'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Posse.objects.count(), 3)


class TestGatewayView(TestCase):
    def setUp(self):
        self.gateway_url = '/api/v1/gateway/'
        self.gateway_status_url = '/api/v1/gateway-status/'
        self.client = APIClient()

        self.posse = Posse.objects.create(label='Posse Label 1')
        self.gateway = Gateway.objects.create(label="Gateway 1",
                                              posse=self.posse,
                                              location="London",
                                              oauth2_client_id="some-random-string",
                                              serial_number="dshjsd-89323")
        self.gateway_status = GatewayStatus.objects.create(gateway=self.gateway,
                                                           hostname='hostname',
                                                           data_flow=True,
                                                           os_name='Macintosh',
                                                           os_version='catalina',
                                                           firmware_version='23923-v',
                                                           maio_edge_version='maybe version 2')

    def test_gateway(self):
        response = self.client.get(path=self.gateway_url, HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        gateway = Gateway.objects.all()
        serializer = GatewaySerializer(gateway, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        
        # since the request is not verbose, test for it
        self.assertEqual(response.data['results'][0]['posse'], self.posse.id)
        self.assertEqual(response.data['results'][0]['status'], [self.gateway_status.id])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test verbose request
        response = self.client.get(path='{}?response=verbose'.format(self.gateway_url),
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['posse'], PosseSerializer(self.posse).data)
        self.assertEqual(response.data['results'][0]['status'], ReferenceGatewayStatusSerializer([self.gateway_status], many=True).data)

        ###### test gateway status
        response = self.client.get(path=self.gateway_status_url,
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        gateway_status = GatewayStatus.objects.all()
        serializer = GatewayStatusSerializer(gateway_status, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['gateway'], self.gateway.id)


        # verbose request
        response = self.client.get(path='{}?response=verbose'.format(self.gateway_status_url),
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['gateway'], ReferenceBaseGatewaySerializer(self.gateway).data)