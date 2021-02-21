from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from data_sources.models import Gateway, Posse


class TestLisAllGatewaysAPI(APITestCase):
    url = reverse("api_v1_endpoints:gateway_endpoints:list-create-gateway")

    def setUp(self) -> None:
        p1 = Posse.objects.create(label="Posse1")
        p2 = Posse.objects.create(label="Posse2")
        Gateway.objects.create(
            label="Gateway1",
            posse=p1,
            location="Banglore",
            oauth2_client_id="djksao008297492",
            serial_number="ABC123",
        )
        Gateway.objects.create(
            label="Gateway2",
            posse=p2,
            location="Delhi",
            oauth2_client_id="djksao234567",
            serial_number="ABC321",
        )

    def test_list_all_gateways(self):
        """
        Test gateway list api
        """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), Gateway.objects.count())

    def test_location_filter(self):
        """
        Test location filter should return filtered results
        """
        query_param = {"location": "Delhi"}
        response = self.client.get(self.url, data=query_param)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)
        self.assertEqual(response.json()["results"][0]["location"], "Delhi")


class TestCreateGatewayAPI(APITestCase):
    url = reverse("api_v1_endpoints:gateway_endpoints:list-create-gateway")

    def setUp(self) -> None:
        self.posse = Posse.objects.create(label="Posse1")
        self.valid_payload = {
            "label": "Gateway1",
            "posse": self.posse.id,
            "location": "Banglore",
            "oauth2_client_id": "djksao008297492",
            "serial_number": "ABC123",
        }
        self.missing_required_field_payload = {
            "label": "Gateway2",
            "location": "Banglore",
            "oauth2_client_id": "1234567890",
            "serial_number": "asdfghjk",
        }
        self.violate_label_serial_number_unique_constraint_payload = {
            "label": "Gateway1",
            "posse": self.posse.id,
            "location": "Banglore",
            "oauth2_client_id": "4567234789",
            "serial_number": "ABC123",
        }
        self.violate_oauth2_client_id_constraint = {
            "label": "Gateway4",
            "posse": self.posse.id,
            "location": "Banglore",
            "oauth2_client_id": "djksao008297492",
            "serial_number": "ABC123",
        }

    def test_create_valid_gateway(self):
        response = self.client.post(self.url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Gateway.objects.count(), 1)
        created_gateway = Gateway.objects.first().label
        self.assertEqual(created_gateway, "Gateway1")

    def test_create_fails_on_missing_required_field(self):
        """
        Test API should throw validation error on missing required field
        """

        response = self.client.post(
            self.url, self.missing_required_field_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_fails_on_duplicate_serial_number_and_label(self):
        """
        Test API should throw validation error on violating unique together constraint for serial number and
        label
        """

        valid_payload = {
            "label": "Gateway1",
            "posse": self.posse,
            "location": "Banglore",
            "oauth2_client_id": "djksao008297492",
            "serial_number": "ABC123",
        }
        # create first gateway with serial_number = ABC123
        Gateway.objects.create(**valid_payload)

        # Call API to create another gateway with serial_number = ABC123
        response = self.client.post(
            self.url,
            self.violate_label_serial_number_unique_constraint_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_fails_for_duplicate_oauth2_client_id(self):
        """
        Test API should throw validation error on duplicate oauth2_client_id
        """
        valid_payload = {
            "label": "Gateway1",
            "posse": self.posse,
            "location": "Banglore",
            "oauth2_client_id": "djksao008297492",
            "serial_number": "ABC123",
        }
        # create first gateway with "oauth2_client_id": "djksao008297492"
        Gateway.objects.create(**valid_payload)

        # Call API to create another gateway with "oauth2_client_id": "djksao008297492"
        response = self.client.post(
            self.url, self.violate_oauth2_client_id_constraint, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_response = {
            "oauth2_client_id": ["gateway with this oauth2 client id already exists."]
        }
        self.assertEqual(response.json(), error_response)
