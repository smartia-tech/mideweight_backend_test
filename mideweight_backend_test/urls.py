"""mideweight_backend_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from data_sources.views import (
    GatewayListCreateAPIView,
    GatewayRetrieveUpdateDestroyAPIView,
    GatewayStatusListAPIView,
    GatewayStatusRetrieveUpdateDestroyAPIView, PossListCreateAPIView,
    PossRetrieveUpdateDestroyAPIView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Smartia Tech API",
        default_version="v1",
        description="""
        Smartia Tech API Doucmentaion
        The `swagger-ui` view can be found [here](/swagger).
        The `ReDoc` view can be found [here](/redoc).
        The swagger YAML document can be found [here](/swagger.yaml).
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

gateway_endpoints = (
    [
        path("", GatewayListCreateAPIView.as_view(), name="list-create-gateway"),
        path(
            "<int:pk>",
            GatewayRetrieveUpdateDestroyAPIView.as_view(),
            name="retrieve-update-destroy-gateway",
        ),
        path("posses", PossListCreateAPIView.as_view(), name="list-create-posse"),
        path(
            "posses/<int:pk>",
            PossRetrieveUpdateDestroyAPIView.as_view(),
            name="get-update-destroy-posse",
        ),
        path(
            "<int:pk>/statuses",
            GatewayStatusListAPIView.as_view(),
            name="list-create-gateway-status",
        ),
        path(
            "<int:gateway_id>/statuses/<int:pk>",
            GatewayStatusRetrieveUpdateDestroyAPIView.as_view(),
            name="retrieve-update-destroy-gateway-status",
        ),
    ],
    "gateway_endpoints",
)

api_v1_endpoints = ([path("gateways/", include(gateway_endpoints))], "api_v1_endpoints")

urlpatterns = [
    path(
        r"swagger(?P<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        r"swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(r"redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_v1_endpoints)),
]
