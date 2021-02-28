from django.contrib import admin

from data_sources.models import Gateway, GatewayStatus, GatewayTag, Posse

admin.site.register(Gateway)
admin.site.register(GatewayStatus)
admin.site.register(GatewayTag)
admin.site.register(Posse)
