from django.urls import path
from . import views


urlpatterns = [
    path(
        "posse/", views.PosseView.as_view(), name="posse_view"
    ),
    path(
        "gateway/", views.GatewayView.as_view(),
        name="gateway_view"
    ),
    path(
        "gateway_status", views.GatewayStatusView.as_view(),
        name="gateway_status_view"
    ),
    path(
        "gateway_tag", views.GatewayTagView.as_view(),
        name="gateway_tag_view"
    ),
]
