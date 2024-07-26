from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db import transaction

from backend.app.serializers.integration import (
    IntegrationSerializer,
    IntegrationUpdateSerializer,
    IntegrationBulkDeleteSerializer,
)
from core.factories.integration import (
    CreateIntegrationUseCaseFactory,
    UpdateIntegrationUseCaseFactory,
    ListIntegrationUseCaseFactory,
    RetrieveIntegrationUseCaseFactory,
    DeleteIntegrationUseCaseFactory,
    BulkDeleteIntegrationUseCaseFactory,
)
from backend.app.exceptions.integration import (
    integration_exception_map,
)


integration_response_schema = openapi.Response(
    'Response description',
    IntegrationSerializer
)
integration_list_schema = openapi.Response(
    'Response description',
    IntegrationSerializer(many=True)
)


class IntegrationView(APIView):
    def create_integration(self, request):
        create_integration_use_case = CreateIntegrationUseCaseFactory.get()
        create_integration_use_case.set_params(
            integration_data=request.data
        )
        response_data = create_integration_use_case.execute()
        return Response(response_data, status=status.HTTP_201_CREATED)

    def update_integration(self, request, pk):
        update_integration_use_case = UpdateIntegrationUseCaseFactory.get()

        try:
            update_integration_use_case.set_params(
                integration_id=pk,
                integration_data=request.data
            )
            response_data = update_integration_use_case.execute()
        except tuple(integration_exception_map.keys()) as e:
            api_exception = integration_exception_map[type(e)]
            raise api_exception
        return Response(response_data, status=status.HTTP_200_OK)

    def list_integration(self, request):
        list_integration_use_case = ListIntegrationUseCaseFactory.get()

        try:
            response_data = list_integration_use_case.execute()
        except tuple(integration_exception_map.keys()) as e:
            api_exception = integration_exception_map[type(e)]
            raise api_exception
        return Response(response_data, status=status.HTTP_200_OK)

    def retrieve_integration(self, request, pk):
        retrieve_integration_use_case = RetrieveIntegrationUseCaseFactory.get()

        try:
            retrieve_integration_use_case.set_params(integration_id=pk)
            response_data = retrieve_integration_use_case.execute()
        except tuple(integration_exception_map.keys()) as e:
            api_exception = integration_exception_map[type(e)]
            raise api_exception
        return Response(response_data, status=status.HTTP_200_OK)

    def delete_integration(self, request, pk):
        delete_integration_use_case = DeleteIntegrationUseCaseFactory.get()

        try:
            delete_integration_use_case.set_params(integration_id=pk)
            delete_integration_use_case.execute()
        except tuple(integration_exception_map.keys()) as e:
            api_exception = integration_exception_map[type(e)]
            raise api_exception
        return Response(status=status.HTTP_204_NO_CONTENT)

    def bulk_delete_integration(self, request):
        bulk_delete_integration_use_case = BulkDeleteIntegrationUseCaseFactory.get()

        try:
            bulk_delete_integration_use_case.set_params(integration_ids=request.data["ids"])
            bulk_delete_integration_use_case.execute()
        except tuple(integration_exception_map.keys()) as e:
            api_exception = integration_exception_map[type(e)]
            raise api_exception
        return Response(status=status.HTTP_204_NO_CONTENT)


class IntegrationListView(IntegrationView):
    @swagger_auto_schema(
        tags=["Integration"],
        request_body=IntegrationSerializer,
        responses={201: integration_response_schema},
    )
    @transaction.atomic
    def post(self, request):
        serializer = IntegrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().create_integration(request=request)

    @swagger_auto_schema(
        tags=["Integration"],
        responses={200: integration_list_schema},
    )
    def get(self, request):
        return super().list_integration(request=request)

    @swagger_auto_schema(
        tags=["Integration"],
        request_body=IntegrationBulkDeleteSerializer,
        responses={204: "No Content"},
    )
    @transaction.atomic
    def delete(self, request):
        serializer = IntegrationBulkDeleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().bulk_delete_integration(request=request)


class IntegrationDetailView(IntegrationView):
    @swagger_auto_schema(
        tags=["Integration"],
        request_body=IntegrationUpdateSerializer,
        responses={200: integration_response_schema},
    )
    @transaction.atomic
    def put(self, request, pk):
        return super().update_integration(request=request, pk=pk)

    @swagger_auto_schema(
        tags=["Integration"],
        responses={200: integration_response_schema},
    )
    def get(self, request, pk):
        return super().retrieve_integration(request=request, pk=pk)

    @swagger_auto_schema(
        tags=["Integration"],
    )
    @transaction.atomic
    def delete(self, request, pk):
        return super().delete_integration(request=request, pk=pk)
