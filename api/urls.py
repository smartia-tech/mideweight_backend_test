from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _
from rest_framework.routers import DefaultRouter

from api.views import PosseView

router = DefaultRouter()
router.register(r'posse', PosseView)

urlpatterns = [
    url(_(r''), include(router.urls)),
]
