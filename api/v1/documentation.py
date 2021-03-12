__author__ = 'Sunday Alexander'

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os
from drf_yasg.generators import OpenAPISchemaGenerator

"""
Swagger Documentation Definition Begins here
"""


class SchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super(SchemaGenerator, self).get_schema(request, public)
        schema.basePath = os.path.join(schema.basePath, 'api/v1/')
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="SMARTIA API",
        default_version='v1',
        description="Smartia Api Version 1.0"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    urlconf="api.v1.urls",
    generator_class=SchemaGenerator,
)