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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


describe = '''
This is a sample api from smartia for consumers to query some factory data, please note that the api responses are paginated,
and also this api is throttled for annonymous users, hence anonymous users will only be able to make 50 unthrottled requests per day. 
we have tried to provide as much information for front end developers and data scientists and made sure that our datetime responses are also formated.
please reach out if you encounter any difficulty using the api. :)
'''
schema_view = get_schema_view(
   openapi.Info(
      title="Smartia-Test V1",
      default_version='v1',
      description=describe,
      contact=openapi.Contact(email="prometheus@smartia.support"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('data_sources.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
