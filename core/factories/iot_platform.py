from core.usecases.iot_platform import (
    ListDeviceDataByIntegrationIdUseCase,
    ExtractDeviceDataUsecase,
    ExtractAllIntegrationsDeviceDataUsecase,
    UpdateDeviceAttributeUsecase,
)
from core.services.iot_platform import ThingsboardClient
from core.db_repos.iot_platform import DeviceDataRepo
from core.factories.integration import IntegrationRepoFactory


class ThingsboardClientFactory:
    @staticmethod
    def get() -> ThingsboardClient:
        return ThingsboardClient()


class DeviceDataRepoFactory:
    @staticmethod
    def get() -> DeviceDataRepo:
        return DeviceDataRepo()


class ListDeviceDataByIntegrationIdUseCaseFactory:
    @staticmethod
    def get() -> ListDeviceDataByIntegrationIdUseCase:
        device_data_repo = DeviceDataRepoFactory.get()

        return ListDeviceDataByIntegrationIdUseCase(
            device_data_repo=device_data_repo,
        )


class ExtractDeviceDataUsecaseFactory:
    @staticmethod
    def get() -> ExtractDeviceDataUsecase:
        device_data_repo = DeviceDataRepoFactory.get()
        integration_repo = IntegrationRepoFactory.get()
        iot_platform_client = ThingsboardClientFactory.get()

        return ExtractDeviceDataUsecase(
            device_data_repo=device_data_repo,
            integration_repo=integration_repo,
            iot_platform_client=iot_platform_client,
        )


class ExtractAllIntegrationsDeviceDataUsecaseFactory:
    @staticmethod
    def get() -> ExtractAllIntegrationsDeviceDataUsecase:
        integration_repo = IntegrationRepoFactory.get()
        extract_device_data_usecase = ExtractDeviceDataUsecaseFactory.get()

        return ExtractAllIntegrationsDeviceDataUsecase(
            integration_repo=integration_repo,
            extract_device_data_usecase=extract_device_data_usecase
        )


class UpdateDeviceAttributeUseCaseFactory:
    @staticmethod
    def get() -> UpdateDeviceAttributeUsecase:
        iot_platform_client = ThingsboardClientFactory.get()

        return UpdateDeviceAttributeUsecase(
            iot_platform_client=iot_platform_client,
        )

