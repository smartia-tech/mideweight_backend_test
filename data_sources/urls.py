
from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GatewayViewSet, PosseViewSet, GatewayStatusViewSet, GatewayTagViewSet

app_name = ""

router = DefaultRouter()
router.register(r"gateway", GatewayViewSet)
router.register(r"posse", PosseViewSet)
router.register(r"gateway-status", GatewayStatusViewSet)
router.register(r"gateway-tags", GatewayTagViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
]
