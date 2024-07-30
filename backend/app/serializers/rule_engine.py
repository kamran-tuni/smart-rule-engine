from rest_framework import serializers

from backend.app.models import RuleChain


class GenerateRuleChainSerializer(serializers.Serializer):
    user_prompt = serializers.CharField()
    chat_history = serializers.ListField(
        child=serializers.JSONField(), required=False, default=[]
    )
    integration_id = serializers.IntegerField()
    is_generated = serializers.BooleanField(required=False, default=False)


class RuleChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleChain
        fields = ['id', 'name', 'nodes', 'integration_id']
