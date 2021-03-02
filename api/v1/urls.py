from django.urls import path, include

urlpatterns = [
    path('datasource/', include('data_sources.api.v1.urls'))
]
