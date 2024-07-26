from django.core.management.base import BaseCommand
from backend.tenant.models import Client


class Command(BaseCommand):
    help = 'Add core tenant'

    def handle(self, *args, **options):
        tenant = Client(
            schema_name='public',
            name='Core Tenant'
        )
        tenant.save()
