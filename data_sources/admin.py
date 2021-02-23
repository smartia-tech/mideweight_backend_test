from django.contrib import admin

# Register your models here.
from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag

admin.site.register(Posse)
admin.site.register(Gateway)
admin.site.register(GatewayStatus)
admin.site.register(GatewayTag)
