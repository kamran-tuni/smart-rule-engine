import uuid

from django.db import models
from django.db.models import JSONField


class Integration(models.Model):
    INTEGRATION_TYPES = [
        ('thingsboard', 'Thingsboard'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=INTEGRATION_TYPES)
    base_url = models.CharField(max_length=255)
    api_key = models.CharField(max_length=1024)
    last_extraction_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class DeviceData(models.Model):
    device_id = models.UUIDField()
    name = models.CharField(max_length=255)
    parameters = JSONField()

    integration = models.ForeignKey(Integration, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
