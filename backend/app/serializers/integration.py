from rest_framework import serializers
from backend.app.models import Integration


class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        fields = ['id', 'name', 'type', 'base_url', 'api_key']


class IntegrationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        fields = ['name', 'type', 'base_url', 'api_key']


class IntegrationBulkDeleteSerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField())
