from django.urls import reverse
from django.test import (
    Client,
    TestCase,
)

from data_sources.models import (
    Gateway,
    Posse,
)


class ApiTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_gateway_tags_listing(self):
        """
        Tests that an http404 is returned when requesting the tags of a
        unexisting Gateway record or when the Gateway instace has no GatewayTag
        records associated with it
        """
        posse = Posse(label='test_label')
        gateway = Gateway(
            label='test_label',
            location='test_location',
            oauth2_client_id='test_client_id',
            serial_number='test_serial_number',
            posse=posse,
        )
        unexisting_gateway_url = reverse('api:gateway-tags', args=['999'])
        existing_gateway_without_tags_url = reverse(
            'api:gateway-tags',
            args=[gateway.pk],
        )

        unexisting_gateway_response = self.client.get(unexisting_gateway_url)
        existing_gateway_without_tags_response = self.client.get(
            existing_gateway_without_tags_url,
        )

        self.assertEqual(
            404,
            unexisting_gateway_response.status_code,
        )
        self.assertEqual(
            404,
            existing_gateway_without_tags_response.status_code,
        )
