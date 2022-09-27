from django.contrib import admin

# Register your models here.

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


# Register your models here.

class PosseAdmin(admin.ModelAdmin):
    list_display = ('label',)
    search_fields = ('label', )


class GatewayAdmin(admin.ModelAdmin):
    list_display = ('label', 'posse', 'location')
    readonly_fields = ('created_at', 'updated_at')


class GatewayTagAdmin(admin.ModelAdmin):
    list_display = ('label', 'gateway', 'data_flow', 'status')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('data_flow', 'status')


class GatewayStatusAdmin(admin.ModelAdmin):
    list_display = ('gateway', 'hostname', 'data_flow', 'os_name', 'os_version',)
    readonly_fields = ('created_at',)
    list_editable = ('data_flow',)


admin.site.register(Posse, PosseAdmin)
admin.site.register(Gateway, GatewayAdmin)
admin.site.register(GatewayStatus, GatewayStatusAdmin)
admin.site.register(GatewayTag, GatewayTagAdmin)
