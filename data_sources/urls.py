from django.urls import path

from data_sources.views import (GatewayDetail, GatewayList,
                                GatewayStatusDetail, GatewayStatusList,
                                GatewayTagDetail, GatewayTagList, PosseDetail,
                                PosseList)

app_name = 'data_sources'

urlpatterns = [
    path('posse/', PosseList.as_view(), name='posse_list'),
    path('posse/<int:pk>/', PosseDetail.as_view(), name='posse_detail'),
    path('gateway/', GatewayList.as_view(), name='gateway_list'),
    path('gateway/<int:pk>/', GatewayDetail.as_view(), name='gateway_detail'),
    path('gateway_status/',
         GatewayStatusList.as_view(),
         name='gateway_status_list'),
    path('gateway_status/<int:pk>/',
         GatewayStatusDetail.as_view(),
         name='gateway_status_detail'),
    path('gateway_tag/', GatewayTagList.as_view(), name='gateway_tag_list'),
    path('gateway_tag/<int:pk>/',
         GatewayTagDetail.as_view(),
         name='gateway_tag_detail'),
]
