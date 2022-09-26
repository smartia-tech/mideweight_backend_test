from django.urls import path, include
from . import views

urlpatterns = [
    path('posse/', views.PosseView.as_view(), name='posse'),
    path('posse/<int:pk>/', views.PosseDetailView.as_view(), name='posse-detail'),
    path('gateway/', views.GatewayView.as_view(), name='gateway'),
    path('gateway/<int:pk>/', views.GatewayDetailView.as_view(), name='gateway-detail'),
    path('gatewaystatus/', views.GatewayStatusView.as_view(), name='gateway-status'),
    path('gatewaystatus/<int:pk>/', views.GatewayStatusDetailView.as_view(), name='gateway-status-detail'),
    path('gatewaytag/', views.GatewayTagView.as_view(), name='gateway-tag'),
    path('gatewaytag/<int:pk>/', views.GatewayTagDetailView.as_view(), name='gateway-tag-detail'),
]