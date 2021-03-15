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
# DRF and Django Imports
from django.contrib import admin
from django.urls import path, include
# Import Views
from data_sources import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/gateway_tags/', views.GatewayTagAPIView.as_view(), name='gateway_tags'),
    path('api/gateways/', views.GatewayApiView.as_view(), name='gateways'),
    path('api/gateway_per_client/', views.ClientGatewayApiView.as_view(), name='gateway_per_client'),
    path('api/gateway_status/', views.GatewayStatusApiView.as_view(), name='gateway_status'),
    path('api/posse/', views.PosseApiView.as_view(), name='posse'),

]
