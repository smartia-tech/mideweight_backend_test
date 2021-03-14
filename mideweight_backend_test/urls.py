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
from data_sources import views



urlpatterns = [
    path('', views.index, name='index'),
    path('posse/', views.posse, name='posse'),
    path('gateway/', views.gateway, name='gateway'),
    path('status/', views.status, name='status'),
    path('tag/', views.tag, name='tag'),
    path('admin/', admin.site.urls),
    path('api/posse/', views.PosseViewList.as_view()),
    path('api/gateway/', views.GatewayViewList.as_view()),
    path('api/status/', views.GatewayStatusViewList.as_view()),
    path('api/tag/', views.GatewayTagViewList.as_view()),
]
