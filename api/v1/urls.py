__author__ = 'Sunday Alexander'

from django.urls import path
from rest_framework import routers
from api.v1.documentation import schema_view
from api.v1.views import GatewayStatusView, GatewayView, PosseView, GatewayTagView

router = routers.DefaultRouter()
router.register(r'gateway', GatewayView, 'gateway')
router.register(r'gateway-status', GatewayStatusView, 'gateway-status')
router.register(r'gateway-tag', GatewayTagView, 'gateway-tag')
router.register(r'posse', PosseView, basename='posse')

app_name = "api.v1"
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += router.urls

