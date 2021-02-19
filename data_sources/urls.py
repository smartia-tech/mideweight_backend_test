from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _
from rest_framework.routers import DefaultRouter

import data_sources.views

router = DefaultRouter()
router.register(r'posse', data_sources.views.PosseView)

urlpatterns = [
    url(_(r''), include(router.urls), name='posse'),
]
