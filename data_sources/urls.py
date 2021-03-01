from django.urls import path
from .views import PosseList, PosseDetail, GatewayList, GatewayDetail, GatewayStatusList, GatewayStatusDetail, \
    GatewayTagList, GatewayTagDetail

urlpatterns = [
    path('posse/', PosseList.as_view(), name='list-create-posse'),
    path('posse/<int:pk>/', PosseDetail.as_view(), name='get-update-destroy-posse'),

    path('gateway/', GatewayList.as_view(), name='list-create-gateway'),
    path('gateway/<int:pk>/', GatewayDetail.as_view(), name='get-update-destroy-gateway'),

    path('gateway/status/', GatewayStatusList.as_view(), name='list-create-gateway-status'),
    path('gateway/status/<int:pk>/', GatewayStatusDetail.as_view(), name='get-update-destroy-gateway-status'),

    path('gateway/tag/', GatewayTagList.as_view(), name='list-create-gateway-tag'),
    path('gateway/tag/<int:pk>/', GatewayTagDetail.as_view(), name='get-update-destroy-gateway-tag'),

]
