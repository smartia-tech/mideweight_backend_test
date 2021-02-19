from django.urls import path, include

from data_sources.views import GatewaysView

gateway_list = GatewaysView.as_view({
    'get': 'list'
})

gateway_retrive = GatewaysView.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('gateways/', gateway_list, name='gateway-list'),
    path('gateways/<int:pk>/', gateway_retrive, name='gateway')
]