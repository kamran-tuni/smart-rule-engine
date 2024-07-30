from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db import transaction

from backend.app.serializers.rule_engine import (
    RuleChainSerializer,
    GenerateRuleChainSerializer,
)

from core.factories.rule_engine import (
    ListRuleChainUseCaseFactory,
    RetrieveRuleChainUseCaseFactory,
    DeleteRuleChainUseCaseFactory,
    GenerateRuleChainUseCaseFactory
)
from backend.app.exceptions.rule_engine import rule_engine_exception_map


rule_chain_response_schema = openapi.Response(
    'Response description',
    RuleChainSerializer
)

rule_chain_list_schema = openapi.Response(
    'Response description',
    RuleChainSerializer(many=True)
)


class RuleChainView(APIView):
    def list_rule_chain(self, request):
        list_rule_chain_use_case = ListRuleChainUseCaseFactory.get()

        try:
            response_data = list_rule_chain_use_case.execute()
        except tuple(rule_engine_exception_map.keys()) as e:
            api_exception = rule_engine_exception_map[type(e)]
            raise api_exception
        return Response(response_data, status=status.HTTP_200_OK)

    def retrieve_rule_chain(self, request, pk):
        retrieve_rule_chain_use_case = RetrieveRuleChainUseCaseFactory.get()

        try:
            retrieve_rule_chain_use_case.set_params(rule_chain_id=pk)
            response_data = retrieve_rule_chain_use_case.execute()
        except tuple(rule_engine_exception_map.keys()) as e:
            api_exception = rule_engine_exception_map[type(e)]
            raise api_exception
        return Response(response_data, status=status.HTTP_200_OK)

    def delete_rule_chain(self, request, pk):
        delete_rule_chain_use_case = DeleteRuleChainUseCaseFactory.get()

        try:
            delete_rule_chain_use_case.set_params(rule_chain_id=pk)
            delete_rule_chain_use_case.execute()
        except tuple(rule_engine_exception_map.keys()) as e:
            api_exception = rule_engine_exception_map[type(e)]
            raise api_exception
        return Response(status=status.HTTP_204_NO_CONTENT)


class RuleChainListView(RuleChainView):
    @swagger_auto_schema(
        tags=["RuleChain"],
        responses={200: rule_chain_list_schema},
    )
    def get(self, request):
        return super().list_rule_chain(request=request)


class RuleChainDetailView(RuleChainView):
    @swagger_auto_schema(
        tags=["RuleChain"],
        responses={200: rule_chain_response_schema},
    )
    def get(self, request, pk):
        return super().retrieve_rule_chain(request=request, pk=pk)

    @swagger_auto_schema(
        tags=["RuleChain"],
    )
    @transaction.atomic
    def delete(self, request, pk):
        return super().delete_rule_chain(request=request, pk=pk)


class GenerateRuleChainView(APIView):
    @swagger_auto_schema(
        tags=["Generate Rule Chain"],
        request_body=GenerateRuleChainSerializer,
        responses={200: GenerateRuleChainSerializer},
    )
    @transaction.atomic
    def post(self, request):
        serializer = GenerateRuleChainSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        generate_rule_chain_use_case = GenerateRuleChainUseCaseFactory.get()

        generate_rule_chain_use_case.set_params(
            data=request.data
        )
        response_data = generate_rule_chain_use_case.execute()
        return Response(response_data, status=status.HTTP_200_OK)
