from typing import List

from django.test import TestCase

# Create your tests here.
from model_bakery import baker
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory, APIClient

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


class TestModels(TestCase):

	def test_posse_model(self):
		posse = baker.make(Posse, label="posse label")
		assert isinstance(posse, Posse)
		self.assertEqual(posse.label, "posse label")

	def test_gateway_model(self):
		gateway = baker.make(Gateway, label="dummy label")
		assert isinstance(gateway, Gateway)
		self.assertEqual(gateway.id, 1)
		self.assertEqual(str(gateway), "dummy label")
		self.assertEqual(gateway.posse_id, 1)

	def test_gateway_status_model(self):
		gateway_status = baker.make(GatewayStatus, hostname="gateway.com")
		assert isinstance(gateway_status, GatewayStatus)
		self.assertEqual(gateway_status.id, 1)
		self.assertEqual(gateway_status.gateway_id, 1)

	def test_gateway_tag_model(self):
		tag = baker.make(GatewayTag, hardware_name="arduino-APC")
		assert isinstance(tag, GatewayTag)
		self.assertEqual(tag.id, 1)
		self.assertEqual(tag.gateway_id, 1)
		self.assertEqual(tag.hardware_name, 'arduino-APC')


class TestGatewayView(TestCase):
	def setUp(self):
		self.gateway_url = '/api/v1/gateway/'
		self.gateway_status_url = '/api/v1/gateway-status/'
		self.gateway_tag_url = '/api/v1/gateway-tags/'
		self.client = APIClient()

		self.posse = baker.make(Posse, label='First Posse Label')
		self.gateway = baker.make(Gateway, label="First Gateway",
		                          posse=self.posse,
		                          location="London",
		                          )
		self.gateway_status = baker.make(GatewayStatus, gateway=self.gateway,
		                                 hostname='First Hostname',
		                                 data_flow=True,
		                                 )
		self.gateway_tag = baker.make(GatewayTag, label='New tag',
		                              gateway=self.gateway,
		                              data_flow=True,
		                              status=GatewayTag.STATUSES[0][0],
		                              unit_type=GatewayTag.UNIT_TYPES[0][1],
		                              )

	def test_fetch_all_gateway(self):
		response = self.client.get(path=self.gateway_url)
		self.assertEqual(response.data['results'][0]['posse']['id'], self.posse.id)
		self.assertEqual(response.data['results'][0]['tags'][0]['id'], self.gateway_tag.id)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_search_gateway_not_exist(self):
		response = self.client.get(path=f'{self.gateway_url}?search=not-exist')
		self.assertEqual(len(response.data['results']), 0)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_search_gateway_exist(self):
		response = self.client.get(path=f'{self.gateway_url}?search={self.gateway.label}')
		self.assertEqual(response.data['results'][0]['posse']['id'], self.posse.id)
		self.assertEqual(response.data['results'][0]['tags'][0]['id'], self.gateway_tag.id)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_gateway_status(self):
		response = self.client.get(path=self.gateway_status_url)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['results'][0]['hostname'], self.gateway_status.hostname)

	def test_gateway_tags_exist(self):
		response = self.client.get(path=f'{self.gateway_tag_url}?search={self.gateway_tag.status}')
		self.assertEqual(len(response.data['results']), 1)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_gateway_tags_not_exist(self):
		response = self.client.get(path=f'{self.gateway_tag_url}?search=inactive')
		self.assertEqual(len(response.data['results']), 0)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	# test filter tags
	def test_gateway_tags_filter(self):
		response = self.client.get(path=f'{self.gateway_tag_url}?unit_type=INVALID_TYPE')

		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.data, {'unit_type':
			[ErrorDetail(
				string='Select a valid choice. INVALID_TYPE is not one of the available choices.',
				code='invalid_choice')]})

	def test_gateway_tag_filter_does_not_exist(self):
		response = self.client.get(path=f'{self.gateway_tag_url}?status=INVALID_STATUS')

		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.data, {'status':
			                                 [ErrorDetail(string='Select a valid choice.'
			                                                     ' INVALID_STATUS is not one of the available choices.',
			                                              code='invalid_choice')]})

	def test_gateway_tag_filter_exist(self):
		response = self.client.get(path=f'{self.gateway_tag_url}?status={self.gateway_tag.status}')

		self.assertEqual(len(response.data['results']), 1)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
