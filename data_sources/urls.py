from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'posse', PosseView, basename='posse')
router.register(r'gateway', GatewayView, basename='gateway')
router.register(r'gateway/status', GatewayStatusView, basename='gateway_status')
router.register(r'gateway/tag', GatewayTagView, 'gateway_tag')

urlpatterns = [
    url(r'^', include(router.urls)),
]