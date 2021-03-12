__author__ = 'Sunday Alexander'

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from data_sources.models import Gateway, Posse

"""
UTILITY CLASS/FUNCTIONS DEFINITIONS BEGIN HERE
"""
User = get_user_model()


# Create user class definition begins here...
class CreateUser:

    def create(self):
        return User.objects.create_user(email="root@smartia.com", username="root", password="rootpa$$")


"""
BASE TEST CASE DEFINITION BEGINS HERE..
"""


class BaseTestCase(APITestCase):

    def setUp(self):
        user = CreateUser().create()

        self.client.login(
            username=user.username,
            password='rootpa$$'
        )


"""
POSSE TEST CASE DEFINITION BEGINS HERE..
"""


class PosseTestcase(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.posse = Posse.objects.create(label='POS')

    def test_create(self):
        post_url = reverse('api.v1:posse-list')
        data = {
            'label': "POS"
        }
        response = self.client.post(post_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        get_url = reverse('api.v1:posse-list')
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        get_url = reverse('api.v1:posse-detail', args=(self.posse.pk,))
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.posse.pk)
        self.assertEqual(response.data['label'], 'POS')


"""
GATEWAY TEST CASE DEFINITION BEGINS HERE..
"""


class GatewayTestcase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.posse = Posse.objects.create(label="POS")
        self.gateway = Gateway.objects.create(
            label='Gateway', posse=self.posse,
            location="Lagos", oauth2_client_id="1",
            serial_number="252552"
        )

    def test_create(self):
        post_url = reverse('api.v1:gateway-list')
        data = {
            'label': "LAG",
            'posse': self.posse.pk,
            'location': 'Lagos',
            'oauth2_client_id': '123455',
            'serial_number': '012324334'
        }
        response = self.client.post(post_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        get_url = reverse('api.v1:gateway-list')
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        get_url = reverse('api.v1:gateway-detail', args=(self.gateway.pk,))
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.posse.pk)
        self.assertEqual(response.data['label'], 'Gateway')
        self.assertEqual(response.data['serial_number'], '252552')
        self.assertEqual(response.data['location'], 'Lagos')
