from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from data_sources.serializers import PosseSerializer, GatewaySerializer
from data_sources.models import Posse, Gateway


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
        self.url = '/api/v1/gateway/'
        self.client = APIClient()

        self.posse = posse=Posse.objects.create(label='Posse Label 1')
        Gateway.objects.create(label="Gateway 1",
                               posse=self.posse,
                               location="London",
                               oauth2_client_id="some-random-string",
                               serial_number="dshjsd-89323")

    def test_gateway(self):
        response = self.client.get(path=self.url, HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        gateway = Gateway.objects.all()
        serializer = GatewaySerializer(gateway, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        
        # since the request is not verbose, test for it
        self.assertEqual(response.data['results'][0]['posse'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test verbose request
        response = self.client.get(path='{}?response=verbose'.format(self.url),
                                   HTTP_AUTHORIZATION='Bearer slbnkmdysqpxyzwacwpztjfikptx')

        gateway = Gateway.objects.all()
        serializer = GatewaySerializer(gateway, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['posse'], PosseSerializer(self.posse).data)