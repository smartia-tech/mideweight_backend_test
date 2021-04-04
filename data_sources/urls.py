from django.urls import path
from . import views

urlpatterns = [
    path('posse', views.PosseApiView.as_view(), name="posse"),
    path('posse/<int:pk>', views.PosseDetailApiView.as_view(), name="posse-detail"),
    path('gateway', views.GatewayApiView.as_view(), name="gateway"),
    path('gateway/<int:pk>', views.GatewayDetailApiView.as_view(), name="gateway-detail"),
    path('gateway-tag', views.GatewayTagApiView.as_view(), name="gateway-tag"),
    path('gateway-tag/<int:pk>', views.GatewayTagDetailApiView.as_view(), name="gateway-tag-detail"),
    path('gateway-status', views.GatewayStatusApiView.as_view(), name="gateway-status"),
    path('gateway-status/<int:pk>', views.GatewayStatusDetailApiView.as_view(), name="gateway-status-detail")
]
