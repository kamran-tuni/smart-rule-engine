from django.db import connection
from django_tenants.middleware.main import TenantMainMiddleware
from backend.tenant.models import Client


class CustomTenantMiddleware(TenantMainMiddleware):
    def get_tenant(self, name):
        tenant = Client.objects.get(name=name)
        return tenant

    def process_request(self, request):
        tenant_name = request.COOKIES.get('tenant')

        connection.set_schema_to_public()

        try:
            tenant = self.get_tenant(name=tenant_name)
        except Client.DoesNotExist:
            self.no_tenant_found(request, tenant_name)
            return

        request.tenant = tenant
        connection.set_tenant(request.tenant)
        self.setup_url_routing(request)
