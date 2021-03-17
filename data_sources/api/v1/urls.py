from rest_framework import routers

from data_sources.api.v1.views import (
    GatewayStatusViewSet, GatewayViewSet,
    PosseViewSet, GatewayTagViewSet
)

router = routers.DefaultRouter()
router.register(r'gateway', GatewayViewSet, 'gateway')
router.register(r'gateway-status', GatewayStatusViewSet, 'gateway-status')
router.register(r'gateway-tag', GatewayTagViewSet, 'gateway-tag')
router.register(r'posse', PosseViewSet, basename='posse')
urlpatterns = router.urls
