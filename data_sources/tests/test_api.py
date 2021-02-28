from copy import copy

import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag
from data_sources.tests.factories import PosseFactory, GatewayFactory, GatewayStatusFactory, GatewayTagFactory

pytestmark = pytest.mark.django_db

DATA_SOURCE_FIELDS = ["label", "created_at", "updated_at"]


@pytest.fixture()
def client_api():
    return APIClient()


class ApiTestBase:
    model = None
    factory = None
    basename = None
    create_payload = {}
    update_payload = {}
    expected_fields = []
    required_fields = []
    filter_fields = [("field", {"included": "some_value", "not_included": "other_value"})]

    def test_create(self, client_api):
        url = reverse(f"{self.basename}-list")
        response = client_api.post(url, data=self.create_payload)
        response_data = response.data

        assert response.status_code == status.HTTP_201_CREATED
        assert self.model.objects.filter(id=response_data["id"]).exists()

    def test_create_without_required_fields(self, client_api):
        for required_field in self.required_fields:
            payload = copy(self.create_payload)
            del payload[required_field]
            url = reverse(f"{self.basename}-list")
            response = client_api.post(url, data=payload)
            response_data = response.data

            assert response.status_code == status.HTTP_400_BAD_REQUEST
            assert required_field in response_data
            assert "This field is required" in response_data[required_field][0]

    def test_update(self, client_api):
        factory_object = self.factory()
        url = reverse(f"{self.basename}-detail", args=[factory_object.id])
        response = client_api.patch(url, data=self.update_payload)

        assert response.status_code == status.HTTP_200_OK
        assert self.model.objects.filter(**self.update_payload).exists()

    def test_retrieve(self, client_api):
        factory_object = self.factory()
        url = reverse(f"{self.basename}-detail", args=[factory_object.id])
        response = client_api.get(url)
        response_data = response.data

        assert response.status_code == status.HTTP_200_OK
        assert response_data["id"] == factory_object.id
        assert set(self.expected_fields) == set(response_data.keys())

    def test_delete(self, client_api):
        factory_object = self.factory()
        url = reverse(f"{self.basename}-detail", args=[factory_object.id])
        response = client_api.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not self.model.objects.filter(id=factory_object.id).exists()

    def test_list(self, client_api):
        batch_size = 2
        self.factory.create_batch(batch_size)

        url = reverse(f"{self.basename}-list")
        response = client_api.get(url)
        response_data = response.data["results"]
        assert response.status_code == status.HTTP_200_OK
        assert len(response_data) == batch_size

    def test_list_filtered_results(self, client_api):
        included_object = self.factory()
        not_included_object = self.factory()

        for field_filter in self.filter_fields:
            url = reverse(f"{self.basename}-list")
            response = client_api.get(url, {field_filter: getattr(included_object, field_filter)})
            response_data = response.data["results"]

            assert response.status_code == status.HTTP_200_OK
            assert len(response_data) == 1
            assert response_data[0]["id"] == included_object.id


class TestPosseViewset(ApiTestBase):
    model = Posse
    basename = "posses"
    factory = PosseFactory
    create_payload = {"label": "test_label"}
    update_payload = {"label": "modified_test_label"}
    expected_fields = ["id", "label"]

    def test_list_filtered_results(self, client_api):
        pass


class TestGatewayViewSet(ApiTestBase):
    model = Gateway
    basename = "gateways"
    factory = GatewayFactory
    update_payload = {"label": "modified_test_label"}
    expected_fields = [
      "id",
      "posse",
      "location",
      "oauth2_client_id",
      "serial_number",
      "data_flow",
      "queue_name"
    ] + DATA_SOURCE_FIELDS
    required_fields = ["posse_id", "serial_number", "oauth2_client_id", "location"]
    filter_fields = ["label", "serial_number", "oauth2_client_id"]

    @property
    def create_payload(self):
        return {
            "label": "test_label",
            "posse_id": PosseFactory().id,
            "location": "some_location",
            "oauth2_client_id": "some_oauth_client_id",
            "serial_number": "HQHF-25545"
        }


class TestGatewayStatusViewSet(ApiTestBase):
    model = GatewayStatus
    basename = "gateway-status"
    factory = GatewayStatusFactory
    update_payload = {"hostname": "modified_test_host_name"}
    expected_fields = [
        "id",
        "gateway",
        "hostname",
        "os_name",
        "os_version",
        "firmware_version",
        "maio_edge_version",
        "data_flow",
        "created_at"
    ]
    required_fields = [
        "maio_edge_version",
        "firmware_version",
        "os_version",
        "os_name",
        "gateway_id",
        "hostname"
    ]
    filter_fields = ["os_version"]

    @property
    def create_payload(self):
        return {
            "label": "test_label",
            "os_name": "ubuntu",
            "os_version": "20.0.2",
            "firmware_version": "1.25.2",
            "maio_edge_version": "2.2.2",
            "gateway_id": GatewayFactory().id,
            "data_flow": True,
            "hostname": "test_hardware_name",
        }


class TestGatewayTagViewSet(ApiTestBase):
    model = GatewayTag
    basename = "gateway-tags"
    factory = GatewayTagFactory
    update_payload = {"hardware_name": "modified_test_hardware_name"}
    expected_fields = [
        "id",
        "gateway",
        "data_flow",
        "hardware_name",
        "unit_name",
        "unit_type",
        "status"
    ] + DATA_SOURCE_FIELDS
    required_fields = ["hardware_name", "gateway_id", "unit_type"]
    filter_fields = ["hardware_name", "gateway_id"]

    @property
    def create_payload(self):
        return {
            "label": "test_label",
            "unit_type": "int",
            "gateway_id": GatewayFactory().id,
            "location": "some_location",
            "data_flow": True,
            "hardware_name": "test_hardware_name",
            "serial_number": "HQHF-25545"
        }
