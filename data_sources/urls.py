from django.urls import path, include
from rest_framework import routers
from data_sources import views

router = routers.SimpleRouter()
router.register(r'posse', views.PosseView)
router.register(r'gateways', views.GatewayViewSet)
router.register(r'gateway_statuses', views.GatewayStatusViewSet)
router.register(r'gateway_tags', views.GatewayTagViewSet)

app_name='data_sources'

urlpatterns = [
    path('', include(router.urls))
]