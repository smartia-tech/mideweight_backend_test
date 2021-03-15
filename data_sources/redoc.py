from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import serializers


class SuccessResponseSerializer(serializers.Serializer):
    """
    This is a
    sample
    serializer
    for showing my intent
    """
    id = serializers.CharField(
        help_text=_("This is the `id` of created object.")
    )


class CustomAutoSchema(SwaggerAutoSchema):
    python_template = None
    js_template = None

    def get_operation(self, operation_keys=None):
        assert self.python_template, "All SwaggerAutoSchema class must define python_template"
        assert self.js_template, "All SwaggerAutoSchema class must define js_template"

        operation = super().get_operation(operation_keys)

        # Using django templates to generate the code
        template_context = {
            "request_url": self.request._request.build_absolute_uri(self.path),
        }

        operation.update({
            'x-code-samples': [
                {
                    "lang": "JS",
                    "source": render_to_string(self.js_template, template_context)
                },
                {
                    "lang": "Python",
                    "source": render_to_string(self.python_template, template_context)
                },
            ]
        })
        return operation

    @classmethod
    def responses(cls):
        return {
            201: SuccessResponseSerializer(),
            400: "Bad Request",
        }
