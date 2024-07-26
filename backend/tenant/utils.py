from django_tenants.utils import get_public_schema_name


def is_public_schema(request):
    if request.tenant.schema_name == get_public_schema_name():
        return True
    else:
        return False
