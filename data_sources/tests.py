from abc import ABC, abstractmethod
from django.test import TestCase
from django.contrib.auth import get_user_model
from data_sources.models import (
    Gateway, GatewayStatus, GatewayTag, Posse
)

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
import json

User = get_user_model()


class UserCreate:
    """
    A user creation helper class
    """

    def create(self):
        user = User.objects.create(email="admin@gmail.com", username="admin")
        user.set_password("admin123")
        user.save()
        return user


class ProtectedAPITestCase(APITestCase):
    """
    Logins the user
    """

    def setUp(self):
        user = UserCreate().create()

        self.client.login(
            username=user.username,
            password='admin123'
        )


class PosseTestcase(ProtectedAPITestCase):
    """
    Test cases for Posse
    """

    def setUp(self):
        super().setUp()
        self.posse = Posse.objects.create(label='possee')

    def test_create(self):
        """
        post posse
        """

        post_url = reverse('api_v1:posse-list')
        data = {
            'label': "Hey"
        }
        response = self.client.post(post_url, data=data, format='json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        """test list of posse"""

        get_url = reverse('api_v1:posse-list')
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        """test detail of posse"""

        get_url = reverse('api_v1:posse-detail', args=(self.posse.pk,))
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.posse.pk)
        self.assertEqual(response.data['label'], 'possee')


class GatewayTestcase(ProtectedAPITestCase):
    """
    Test cases for Gateway
    """

    def setUp(self):
        super().setUp()
        self.posse = Posse.objects.create(label="Possee")
        self.gateway = Gateway.objects.create(
            label='Gateway', posse=self.posse,
            location="Nepal", oauth2_client_id="1",
            serial_number="12345"
        )

    def test_create(self):
        """
        post posse
        """

        post_url = reverse('api_v1:gateway-list')
        data = {
            'label': "Hey",
            'posse': self.posse.pk,
            'location': 'Nepal',
            'oauth2_client_id': '123455',
            'serial_number': '012324334'
        }
        response = self.client.post(post_url, data=data, format='json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        """test list of gateway"""

        get_url = reverse('api_v1:gateway-list')
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        """
        get detail of gateway
        """

        get_url = reverse('api_v1:gateway-detail', args=(self.gateway.pk,))
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.posse.pk)
        self.assertEqual(response.data['label'], 'Gateway')
        self.assertEqual(response.data['serial_number'], '12345')
        self.assertEqual(response.data['location'], 'Nepal')
