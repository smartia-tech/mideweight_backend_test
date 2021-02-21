from django.test import TestCase
from data_sources.models import Gateway, GatewayStatus, GatewayTag, Posse
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
import json
# Create your tests here.

class PosseTestcase(APITestCase):
    '''
    testcase for all posse related endpoints
    '''
    def setUp(self):
        Posse.objects.create(label='Australian')
        Posse.objects.create(label='Mexican')
    
    def test_list_posse(self):
        '''
        test enpoint for getting list of posses
        '''
        get_url = reverse('posse-list')
        res = self.client.get(get_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # assert that we only have two instances returned since we only have two created
        self.assertEqual(len(res.data['results']), 2)
    
    def test_detail_posse(self):
        '''
        test enpoint for getting specific posses
        '''
        specific_id = 2
        get_url = reverse('posse-detail', args=(specific_id,))
        res = self.client.get(get_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], specific_id)
        self.assertEqual(res.data['label'], 'Mexican')


class GatewayTestcase(APITestCase):
    '''
    testcase for all gateway related endpoints
    '''

    def setUp(self):
        posse = Posse.objects.create(label='Australian')
        Gateway.objects.create(label='gateway001', location="Australia", oauth2_client_id='12xc34v', serial_number='11213112', posse=posse)
    
    def test_list_gateways(self):
        '''
        test enpoint for getting list of gateways
        '''
        get_url = reverse('gateway-list')
        res = self.client.get(get_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # assert that we only have one instance returned since we only have one created
        self.assertEqual(len(res.data['results']), 1)
    
    def test_detail_gateway(self):
        '''
        test enpoint for getting specific gateway
        '''
        specific_id = 1
        get_url = reverse('gateway-detail', args=(specific_id,))
        res = self.client.get(get_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], specific_id)
        self.assertEqual(res.data['label'], 'gateway001')
    
    def test_search_filter(self):
        '''
        test the search filter feature, users can filter by label, location and posse label
        '''
        get_url = reverse('gateway-list')
        res = self.client.get(get_url, data={'search':'Australian'})
        active_instances = Gateway.objects.filter(posse__label='Australian')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['results']), active_instances.count())


class GatewayStatusTestcase(APITestCase):
    '''
    testcase for all gatewaystatus related endpoints
    '''
    
    def setUp(self):
        posse = Posse.objects.create(label='Australian')
        gateway = Gateway.objects.create(label='gateway001', location="Australia", oauth2_client_id='12xc34v', serial_number='11213112', posse=posse)
        GatewayStatus.objects.create(hostname='host2004', os_name='parrot', os_version=8.4, firmware_version=1.0, maio_edge_version='v2.1', data_flow=True, gateway=gateway)
        GatewayStatus.objects.create(hostname='host2000', os_name='linux', os_version=10.4, firmware_version=1.0, maio_edge_version='v2.1', data_flow=True, gateway=gateway)
    
    def test_list_gatewaystatuses(self):
        '''
        test enpoint for getting list of gatewaystatuses
        '''
        get_url = reverse('gatewaystatus-list')
        res = self.client.get(get_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # assert that we only have one instance returned since we only have one created
        self.assertEqual(len(res.data['results']), 2)
    
    def test_detail_gatewaystatus(self):
        '''
        test enpoint for getting specific gatewaystatus
        '''
        specific_id = 1
        get_url = reverse('gatewaystatus-detail', args=(specific_id,))
        res = self.client.get(get_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], specific_id)
        self.assertEqual(res.data['os_name'], 'parrot')
    
    def test_search_filter(self):
        '''
        test the search filter feature, users can filter by os_name and host_name
        '''
        get_url = reverse('gatewaystatus-list')
        res = self.client.get(get_url, data={'search':'linux'})
        active_instances = GatewayStatus.objects.filter(os_name='linux')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['results']), active_instances.count())


class GatewayTagTestcase(APITestCase):
    '''
    testcase for all gatewaytag related endpoints
    '''
    
    def setUp(self):
        posse = Posse.objects.create(label='Mexican')
        gateway = Gateway.objects.create(label='gateway001', location="Australia", oauth2_client_id='12xc34v', serial_number='11213112', posse=posse)
        GatewayTag.objects.create(label='birdy', hardware_name='birdroni_ec2', unit_name='ec_series', unit_type='float', status='dormant', data_flow=True, gateway=gateway)
        GatewayTag.objects.create(label='perseverance', hardware_name='nasa_xx', unit_name='space_series', unit_type='bool', status='active', data_flow=True, gateway=gateway)
        GatewayTag.objects.create(label='spaceX', hardware_name='tesla_21', unit_name='series_21', unit_type='bool', status='active', data_flow=True, gateway=gateway)


    def test_list_gatewaytag(self):
        '''
        test enpoint for getting list of gatewaystatuses
        '''
        get_url = reverse('gatewaytag-list')
        res = self.client.get(get_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # assert that we only have three instance returned since we only have three created
        self.assertEqual(len(res.data['results']), 3)
    
    def test_detail_gatewaytag(self):
        '''
        test enpoint for getting specific gatewaystatus
        '''
        specific_id = 3
        get_url = reverse('gatewaytag-detail', args=(specific_id,))
        res = self.client.get(get_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], specific_id)
        self.assertEqual(res.data['label'], 'spaceX')
    
    def test_search_filter(self):
        '''
        test the search filter feature, users can filter by status, unit_name and hardware_name
        '''
        get_url = reverse('gatewaytag-list')
        res = self.client.get(get_url, data={'search':'active'})
        active_instances = GatewayTag.objects.filter(status='active')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['results']), active_instances.count())
