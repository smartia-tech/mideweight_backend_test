from rest_framework import routers

from data_sources.api.v1.views import GatewayViewSet

router = routers.DefaultRouter()
router.register(r'getway', GatewayViewSet, basename='gateway')

urlpatterns = router.urls
