import json
from django.urls import reverse
from rest_framework import status
from data_sources.models import Posse
from django.test import TestCase, Client

from data_sources.serializers import PosseSerializer

# initialize the APIClient app
client = Client()


class PosseTest(TestCase):
    """ Test module for GET and Create posse API """

    def setUp(self):
        Posse.objects.create(
            label='Casper')
        Posse.objects.create(
            label='Muffin')
        Posse.objects.create(
            label='Rambo')
        Posse.objects.create(
            label='Ricky')
        self.valid_payload = {
            "label": "test_label"
        }

    def test_get_list_of_posse(self):
        # get API response
        response = client.get(reverse('posse'))
        response_data = json.loads(response.content.decode('utf-8'))

        # get data from db
        possess = Posse.objects.all()
        serializer = PosseSerializer(possess, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("data", response_data)
        self.assertEqual(response_data["data"]["results"], serializer.data)

    def test_get_one_posse(self):
        response = client.get(reverse('posse-detail', args=[1]))
        response_data = json.loads(response.content.decode('utf-8'))
        posse = Posse.objects.get(id=1)
        serializer = PosseSerializer(posse)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("data", response_data)
        self.assertEqual(response_data["data"], serializer.data)

    def test_create_posse(self):
        response = client.post(
            reverse('posse'),
            data=json.dumps(self.valid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_posse_invalid_label(self):
        response = client.post(
            reverse('posse'),
            data=json.dumps(self.valid_payload.pop("label")),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_posse(self):
        self.valid_payload["label"] = "updated label"
        response = client.put(
            reverse('posse-detail', args=[1]),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data["data"]["label"], self.valid_payload["label"])

    def test_delete_posse(self):
        response = client.delete(
            reverse('posse-detail', args=[1])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)