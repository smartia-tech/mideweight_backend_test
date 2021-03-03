from django.contrib import admin

from .models import (
    Gateway,
    GatewayStatus,
    GatewayTag,
    Posse,
)

admin.site.register([
    Gateway,
    GatewayStatus,
    GatewayTag,
    Posse,
])
