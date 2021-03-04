from rest_framework import routers

from .views import (
    GatewayViewSet,
    GatewayTagViewSet,
    GatewayStatusViewSet,
    PosseViewSet,
)

router = routers.DefaultRouter()

router.register(r'gateways', GatewayViewSet, basename='gateway')
router.register(r'tags', GatewayTagViewSet, basename='gatewaytag')
router.register(r'status', GatewayStatusViewSet, basename='gatewaystatus')
router.register(r'posses', PosseViewSet, basename='posse')

urlpatterns = router.urls  # noqa
