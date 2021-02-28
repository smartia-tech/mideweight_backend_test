from rest_framework import routers

from data_sources.views import PosseViewSet, GatewayViewSet, GatewayStatusViewSet, GatewayTagViewSet

router = routers.SimpleRouter()
router.register(r"posses", PosseViewSet, basename="posses"),
router.register(r"gateways", GatewayViewSet, basename="gateways"),
router.register(r"gateway-status", GatewayStatusViewSet, basename="gateway-status"),
router.register(r"gateway-tags", GatewayTagViewSet, basename="gateway-tags"),


urlpatterns = router.urls
