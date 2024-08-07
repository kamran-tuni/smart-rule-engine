from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=255)
    account_id = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    platform = serializers.CharField(max_length=255)
    base_url = serializers.CharField(max_length=255)
    api_key = serializers.CharField(max_length=1024)
