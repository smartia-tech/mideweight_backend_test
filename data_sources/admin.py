from django.contrib import admin

# Register your models here.
from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posse, AuthorAdmin)
admin.site.register(Gateway, AuthorAdmin)
admin.site.register(GatewayStatus, AuthorAdmin)
admin.site.register(GatewayTag, AuthorAdmin)
