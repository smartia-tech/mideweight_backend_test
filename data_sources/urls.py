from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _
from rest_framework.routers import DefaultRouter

import data_sources.views

router = DefaultRouter()
router.register(r'posse', data_sources.views.PosseView)
router.register(r'gateway', data_sources.views.GatewayView)
router.register(r'gateway-status', data_sources.views.GatewayStatusView)
router.register(r'gateway-tags', data_sources.views.GatewayTagView)

urlpatterns = [
    url(_(r''), include(router.urls)),
]
