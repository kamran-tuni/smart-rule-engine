from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from backend.tenant.utils import is_public_schema
from backend.app.models import Integration, DeviceData, RuleChain


@admin.register(Integration)
class IntegrationAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'type')

    def has_module_permission(self,request, view=None):
        return not is_public_schema(request=request)


@admin.register(RuleChain)
class RuleChainAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'Integration_name')

    def Integration_name(self, obj):
        return obj.integration.name

    def has_module_permission(self,request, view=None):
        return not is_public_schema(request=request)


@admin.register(DeviceData)
class DeviceDataAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'Integration_name')

    def Integration_name(self, obj):
        return obj.integration.name

    def has_module_permission(self,request, view=None):
        return not is_public_schema(request=request)
