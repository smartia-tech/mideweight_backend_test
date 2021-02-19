from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from data_sources.serializers import PosseSerializer
from data_sources.models import Posse


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
