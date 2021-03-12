from django.urls import path, include
from rest_framework import routers

from data_sources.views import PosseViewSet, GatewayViewSet, GatewayStatusViewSet, GatewayTagViewSet

router = routers.DefaultRouter()

router.register('posse', PosseViewSet)
router.register('gateway', GatewayViewSet)
router.register('gateway_status', GatewayStatusViewSet)
router.register('gateway_tag', GatewayTagViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
