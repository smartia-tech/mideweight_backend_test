from django.contrib import admin
from .models import (
    Posse, Gateway, GatewayStatus, GatewayTag
)


class PosseAdmin(admin.ModelAdmin):
    list_display = [
        "label"
    ]


admin.site.register(Posse, PosseAdmin)


class GatewayAdmin(admin.ModelAdmin):
    llist_display = [
        "label", "posse", "location",
        "oauth2_client_id", "serial_number",
        "type_name"
    ]


admin.site.register(Gateway, GatewayAdmin)


class GatewayStatusAdmin(admin.ModelAdmin):
    list_display = [
        "gateway", "hostname", "data_flow",
        "os_name", "os_version", "firmware_version",
        "maio_edge_version", "created_at"
    ]


admin.site.register(GatewayStatus, GatewayStatusAdmin)


class GatewayTagAdmin(admin.ModelAdmin):
    list_display = [
        "gateway", "data_flow", "hardware_name",
        "unit_name", "unit_type", "status"
    ]


admin.site.register(GatewayTag, GatewayTagAdmin)
