from django.db import models


class Integration(models.Model):
    INTEGRATION_TYPES = [
        ('thingsboard', 'Thingsboard'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=INTEGRATION_TYPES)
    base_url = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.name
