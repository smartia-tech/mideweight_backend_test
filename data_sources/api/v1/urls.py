from rest_framework import routers

from data_sources.api.v1.views import GatewayViewSet, PosseViewSet

router = routers.DefaultRouter()
router.register(r'gateway', GatewayViewSet, basename='gateway')
router.register(r'posse', PosseViewSet, basename='posse')

urlpatterns = router.urls
