from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from backend.tenant.utils import is_public_schema
from backend.app.models import Integration


@admin.register(Integration)
class IntegrationAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'type')

    def has_module_permission(self,request, view=None):
        return not is_public_schema(request=request)
