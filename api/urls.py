from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _
from rest_framework.routers import DefaultRouter

from api.views import PosseView, GatewayView, GatewayStatusView, GatewayTagView

router = DefaultRouter()
router.register(r'posse', PosseView)
router.register(r'gateway', GatewayView)
router.register(r'gateway-status', GatewayStatusView)
router.register(r'gateway-tags', GatewayTagView)

urlpatterns = [
    url(_(r''), include(router.urls)),
]
