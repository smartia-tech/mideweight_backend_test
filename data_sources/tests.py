from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from data_sources.serializers import PosseSerializer, GatewaySerializer, GatewayStatusSerializer,\
    ReferenceGatewayStatusSerializer, ReferenceBaseGatewaySerializer, ReferenceGatewayTagSerializer,\
    GatewayTagSerializer
from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


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
        self.gateway_tag_url = '/api/v1/gateway-tags/'
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
        self.gateway_tag = GatewayTag.objects.create(label='The gateway tag label',
                                                     gateway=self.gateway,
                                                     data_flow=True,
                                                     hardware_name="The hardware name",
                                                     unit_name="The unit name",
                                                     unit_type=GatewayTag.UNIT_TYPES[0][0],
                                                     status=GatewayTag.STATUSES[0][0])

    def test_gateway(self):
        response = self.client.get(path=self.gateway_url, HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        gateway = Gateway.objects.all()
        serializer = GatewaySerializer(gateway, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        
        # since the request is not verbose, test for it
        self.assertEqual(response.data['results'][0]['posse'], self.posse.id)
        self.assertEqual(response.data['results'][0]['status'], [self.gateway_status.id])
        self.assertEqual(response.data['results'][0]['tags'], [self.gateway_tag.id])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test verbose request
        response = self.client.get(path='{}?response=verbose'.format(self.gateway_url),
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['posse'], PosseSerializer(self.posse).data)
        self.assertEqual(response.data['results'][0]['status'],
                         ReferenceGatewayStatusSerializer([self.gateway_status], many=True).data)
        self.assertEqual(response.data['results'][0]['tags'],
                         ReferenceGatewayTagSerializer([self.gateway_tag], many=True).data)

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


        ##### test gateway tags
        response = self.client.get(path=self.gateway_tag_url,
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')
        gateway_tags = GatewayTag.objects.all()
        serializer = GatewayTagSerializer(gateway_tags, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['gateway'], self.gateway.id)

        # verbose request
        response = self.client.get(path='{}?response=verbose'.format(self.gateway_tag_url),
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['gateway'], ReferenceBaseGatewaySerializer(self.gateway).data)

    def test_search_filter_gateway(self):
        # test gateway
        response = self.client.get(path='{}?search=NA'.format(self.gateway_url),
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')
        self.assertEqual(len(response.data['results']), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(path='{}?search=Gateway 1'.format(self.gateway_url),
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test gateway_status
        response = self.client.get(path='{}?search=NOT EXISTS'.format(self.gateway_status_url),
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')
        self.assertEqual(len(response.data['results']), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(path='{}?search=hostname'.format(self.gateway_status_url),
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test gateway tags
        response = self.client.get(path='{}?search=DOES NOT EXISTS'.format(self.gateway_tag_url),
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')
        self.assertEqual(len(response.data['results']), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(path='{}?search=The hardware'.format(self.gateway_tag_url),
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
