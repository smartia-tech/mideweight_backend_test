from django.urls import path, include

from data_sources.routes import *


urlpatterns = [
    path('posses/', posse_list, name='posse-list'),
    path('posses/<int:pk>/', posse_retrieve, name='posse'),
    path('gateways/', gateway_list, name='gateway-list'),
    path('gateways/<int:pk>/', gateway_retrieve, name='gateway'),
    path('gateway_tags/', gateway_tag_list, name='gateway-tag-list'),
    path('gateway_tags/<int:pk>/', gateway_tag_retrieve, name='gateway-tag'),
    path('gateway_statuses/', gateway_status_list, name='gateway-status-list'),
    path('gateway_statuses/<int:pk>', gateway_status_retrieve, name='gateway-status'),
]