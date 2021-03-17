from django.urls import path, include

app_name = "api_v1"

urlpatterns = [
    path('', include('data_sources.api.v1.urls'))
]
