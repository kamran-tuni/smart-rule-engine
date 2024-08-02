from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from backend.app.exceptions.auth import InvalidUsernameException

from backend.app.serializers.auth import (
    SignupSerializer,
)
from drf_yasg.utils import swagger_auto_schema, status

from django_tenants.utils import schema_context
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password

from rest_framework.permissions import AllowAny
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import (
    Response,
)
from settings import SIMPLE_JWT
from backend.tenant.models import Client

from core.factories.integration import (
    CreateIntegrationUseCaseFactory,
)


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        tags=["Auth"],
    )
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUsernameException

        login(request, user)
        jwt_response = super().post(request, *args, **kwargs)

        response = Response({'detail': 'success'}, status=status.HTTP_200_OK)
        response.set_cookie(
            key=SIMPLE_JWT['AUTH_COOKIE'],
            value=jwt_response.data["access"],
            expires=SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure=SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite=SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        response.set_cookie(
            key='username',
            value=username,
            expires=SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure=SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            samesite=SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )

        return response


class LogoutView(APIView):
    @swagger_auto_schema(
        tags=["Auth"],
    )
    def post(self, request):
        logout(request)

        response = Response({'detail': 'success'}, status=status.HTTP_200_OK)
        response.delete_cookie(SIMPLE_JWT['AUTH_COOKIE'])
        response.delete_cookie('username')

        return response


class SignupView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=["Auth"],
        request_body=SignupSerializer,
    )
    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            client = Client.objects.create(
                name=data['account_id'],
                schema_name=data['account_id'].replace(' ', '')
            )

            with schema_context(client.schema_name):
                User.objects.create(
                    username=data['username'],
                    password=make_password(data['password'])
                )

                create_integration_use_case = CreateIntegrationUseCaseFactory.get()
                create_integration_use_case.set_params(
                    integration_data={
                        'name': data['platform'],
                        'type': data['platform'],
                        'base_url': data['base_url'],
                        'api_key': data['api_key']
                    }
                )
                create_integration_use_case.execute()

            return Response({'detail': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
