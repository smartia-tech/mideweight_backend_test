from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from data_sources.api.views import PosseViewSet, GatewayViewSet, GatewayStatusViewSet, GatewayTagViewSet


router = DefaultRouter()
router.register(r'posse', PosseViewSet)
router.register(r'gateway', GatewayViewSet)
router.register(r'gateway-status', GatewayStatusViewSet)
router.register(r'gateway-tag', GatewayTagViewSet)

urlpatterns = [
    url('', include(router.urls))
]
