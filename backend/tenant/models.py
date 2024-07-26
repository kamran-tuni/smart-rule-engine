import pytz

from django.db import models
from django_tenants.models import TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        app_label = 'tenant'
