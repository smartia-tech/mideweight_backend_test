import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_405_METHOD_NOT_ALLOWED

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag
from data_sources.serializers import (
    PosseSerializer, GatewaySerializer, GatewayTagSerializer, GatewayStatusSerializer
)


factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}

class GatewayTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.posse_list = [
            Posse.objects.create(label="Test Posse"),
            Posse.objects.create(label="Dummy Posse")
        ]
        self.gateway_list = (
            Gateway.objects.create(
                label="Test Gateway",
                posse=self.posse_list[0],
                location="Test Location",
                oauth2_client_id=123,
                serial_number=1234
            ),
            Gateway.objects.create(
                label="Dummy Gateway",
                posse=self.posse_list[1],
                location="Dummy Location",
                oauth2_client_id=0,
                serial_number=0
            )
        )
        self.gateway_tag_list = [
            GatewayTag.objects.create(label='tag1',
                       data_flow=True,
                       gateway=self.gateway_list[0],
                       hardware_name="Hardware1",
                       unit_name="Kilo",
                       unit_type="int",
                       status="Active"),
            GatewayTag.objects.create(label='tag2',
                       data_flow=False,
                       gateway=self.gateway_list[0],
                       hardware_name="Super Hardware",
                       unit_name="Pounds",
                       unit_type="float",
                       status="disabled"),
            GatewayTag.objects.create(label='tag3',
                       data_flow=True,
                       gateway=self.gateway_list[1],
                       hardware_name="Low power hardware",
                       unit_name="Grams",
                       unit_type="str",
                       status="dormant")
        ]
        self.gateway_status_list = [
            GatewayStatus.objects.create(data_flow=True,
                          gateway=self.gateway_list[0],
                          hostname="Basement",
                          os_name="Ubuntu",
                          os_version="20.04",
                          firmware_version="12.3",
                          maio_edge_version="2.2"),
            GatewayStatus.objects.create(data_flow=False,
                          gateway=self.gateway_list[0],
                          hostname="Level 1",
                          os_name="Ubuntu",
                          os_version="18.04",
                          firmware_version="11.9",
                          maio_edge_version="2.0"),
            GatewayStatus.objects.create(data_flow=True,
                          gateway=self.gateway_list[1],
                          hostname="Level 10",
                          os_name="Ubuntu",
                          os_version="19.10",
                          firmware_version="12.1",
                          maio_edge_version="2.1")
        ]
        return super().setUp()

    def test_get_posses(self):
        response = self.client.get(reverse('posse-list'))
        self.assertEqual(HTTP_200_OK, response.status_code)

        posse_list_data = (
            PosseSerializer(self.posse_list, many=True).data
        )
        self.assertEqual(posse_list_data, json.loads(response.content))

    def test_post_posses_method_not_allowed(self):
        response = self.client.post(reverse('posse-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_put_posses_method_not_allowed(self):
        response = self.client.put(reverse('posse-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_delete_posses_method_not_allowed(self):
        response = self.client.delete(reverse('posse-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_get_single_posse_success(self):
        response = self.client.get(reverse('posse', kwargs={'pk': self.posse_list[0].pk}))
        self.assertEqual(HTTP_200_OK, response.status_code)

        posse_data = PosseSerializer(self.posse_list[0]).data
        self.assertEqual(posse_data, json.loads(response.content))

    def test_get_single_posse_not_found(self):
        response = self.client.get(reverse('posse', kwargs={'pk': 10}))
        self.assertEqual(HTTP_404_NOT_FOUND, response.status_code)

    def test_post_single_posse_method_not_allowed(self):
        response = self.client.post(reverse('posse', kwargs={'pk': 10}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_put_single_posse_method_not_allowed(self):
        response = self.client.put(reverse('posse', kwargs={'pk': 10}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_delete_single_posse_method_not_allowed(self):
        response = self.client.delete(reverse('posse', kwargs={'pk': 10}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_get_gateways(self):
        response = self.client.get(reverse('gateway-list'))
        self.assertEqual(HTTP_200_OK, response.status_code)

        gateway_list_data = (
            GatewaySerializer(self.gateway_list, many=True, context=serializer_context).data
        )
        self.assertEqual(gateway_list_data, json.loads(response.content))

    def test_post_gateways_method_not_allowed(self):
        response = self.client.post(reverse('gateway-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_put_gateways_method_not_allowed(self):
        response = self.client.put(reverse('gateway-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_delete_gateways_method_not_allowed(self):
        response = self.client.delete(reverse('gateway-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_get_single_gateway_success(self):
        response = self.client.get(reverse('gateway', kwargs={'pk': self.gateway_list[0].pk}))
        self.assertEqual(HTTP_200_OK, response.status_code)

        gateway_data = (
            GatewaySerializer(self.gateway_list[0], context=serializer_context).data
        )
        self.assertEqual(gateway_data, json.loads(response.content))

    def test_get_single_gateway_not_found(self):
        response = self.client.get(reverse('gateway', kwargs={'pk': 10}))
        self.assertEqual(HTTP_404_NOT_FOUND, response.status_code)

    def test_post_single_gateway_method_not_allowed(self):
        response = self.client.post(reverse('gateway', kwargs={'pk': self.gateway_list[0].pk}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_put_single_gateway_method_not_allowed(self):
        response = self.client.put(reverse('gateway', kwargs={'pk': self.gateway_list[0].pk}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_delete_single_gateway_method_not_allowed(self):
        response = self.client.delete(reverse('gateway', kwargs={'pk': self.gateway_list[0].pk}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_get_gateway_tags(self):
        response = self.client.get(reverse('gateway-tag-list'))
        self.assertEqual(HTTP_200_OK, response.status_code)

        tag_list_data = (
            GatewayTagSerializer(self.gateway_tag_list, many=True, context=serializer_context).data
        )
        self.assertEqual(tag_list_data, json.loads(response.content))

    def test_post_gateway_tags_method_not_allowed(self):
        response = self.client.post(reverse('gateway-tag-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_put_gateway_tags_method_not_allowed(self):
        response = self.client.put(reverse('gateway-tag-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_delete_gateway_tags_method_not_allowed(self):
        response = self.client.delete(reverse('gateway-tag-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_get_signle_gateway_tag_success(self):
        response = self.client.get(reverse('gateway-tag', kwargs={'pk': self.gateway_tag_list[0].pk}))
        self.assertEqual(HTTP_200_OK, response.status_code)

        tag_data = (
            GatewayTagSerializer(self.gateway_tag_list[0], context=serializer_context).data
        )
        self.assertEqual(tag_data, json.loads(response.content))

    def test_get_single_gateway_tag_not_found(self):
        response = self.client.get(reverse('gateway-tag', kwargs={'pk': 10}))
        self.assertEqual(HTTP_404_NOT_FOUND, response.status_code)

    def test_post_single_gateway_tag_method_not_allowed(self):
        response = self.client.post(reverse('gateway-tag', kwargs={'pk': self.gateway_tag_list[0].pk}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_put_single_gateway_tag_method_not_allowed(self):
        response = self.client.put(reverse('gateway-tag', kwargs={'pk': self.gateway_tag_list[0].pk}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_delete_single_gateway_tag_method_not_allowed(self):
        response = self.client.delete(reverse('gateway-tag', kwargs={'pk': self.gateway_tag_list[0].pk}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_get_gateway_statuses(self):
        response = self.client.get(reverse('gateway-status-list'))
        self.assertEqual(HTTP_200_OK, response.status_code)

        status_list_data = (
            GatewayStatusSerializer(self.gateway_status_list, many=True, context=serializer_context).data
        )
        self.assertEqual(status_list_data, json.loads(response.content))

    def test_post_gateway_statuses_method_not_allowed(self):
        response = self.client.post(reverse('gateway-status-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_put_gateway_statuses_method_not_allowed(self):
        response = self.client.put(reverse('gateway-status-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_delete_gateway_statuses_method_not_allowed(self):
        response = self.client.delete(reverse('gateway-status-list'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_get_single_gateway_status_success(self):
        response = self.client.get(reverse('gateway-status', kwargs={'pk': self.gateway_status_list[0].pk}))
        self.assertEqual(HTTP_200_OK, response.status_code)

        status_data = (
            GatewayStatusSerializer(self.gateway_status_list[0], context=serializer_context).data
        )
        self.assertEqual(status_data, json.loads(response.content))

    def test_get_single_gateway_status_not_found(self):
        response = self.client.get(reverse('gateway-status', kwargs={'pk': 10}))
        self.assertEqual(HTTP_404_NOT_FOUND, response.status_code)

    def test_post_single_gateway_status_method_not_allowed(self):
        response = self.client.post(reverse('gateway-status', kwargs={'pk': self.gateway_status_list[0].pk}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_put_single_gateway_status_method_not_allowed(self):
        response = self.client.put(reverse('gateway-status', kwargs={'pk': self.gateway_status_list[0].pk}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_delete_single_gateway_status_method_not_allowed(self):
        response = self.client.delete(reverse('gateway-status', kwargs={'pk': self.gateway_status_list[0].pk}))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)    
