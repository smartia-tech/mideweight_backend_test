from django.urls import path
from data_sources.views import (
    PosseView, PosseDetailView,
    GatewayView, GatewayDetailView,
    GatewayStatusView, GatewayStatusDetailView,
    GatewayTagView, GatewayTagDetailView
)
urlpatterns = [
    path('posses/', PosseView.as_view(), name='posse-list'),
    path('posses/<int:pk>/', PosseDetailView.as_view(), name='posse-detail'),
    path('gateways/', GatewayView.as_view(), name='gateway-list'),
    path('gateways/<int:pk>/', GatewayDetailView.as_view(), name='gateway-detail'),
    path('gatewaystatus/', GatewayStatusView.as_view(), name='gatewaystatus-list'),
    path('gatewaystatus/<int:pk>/', GatewayStatusDetailView.as_view(), name='gatewaystatus-detail'),
    path('gatewaytag/', GatewayTagView.as_view(), name='gatewaytag-list'),
    path('gatewaytag/<int:pk>/', GatewayTagDetailView.as_view(), name='gatewaytag-detail'),
]
