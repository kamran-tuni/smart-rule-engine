from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from backend.tenant.models import Client
from backend.tenant.utils import is_public_schema


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'created_on')

    def has_module_permission(self,request, view=None):
        return is_public_schema(request=request)
