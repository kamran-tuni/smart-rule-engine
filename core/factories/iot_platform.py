from core.usecases.iot_platform import (
    ExtractDeviceDataUsecase,
    UpdateDeviceAttributeUsecase,
)
from core.services.iot_platform import ThingsboardClient


class ThingsboardClientFactory:
    @staticmethod
    def get() -> ThingsboardClient:
        return ThingsboardClient()


class ExtractDeviceDataUsecaseFactory:
    @staticmethod
    def get() -> ExtractDeviceDataUsecase:
        iot_platform_client = ThingsboardClientFactory.get()

        return ExtractDeviceDataUsecase(
            iot_platform_client=iot_platform_client,
        )


class UpdateDeviceAttributeUseCaseFactory:
    @staticmethod
    def get() -> UpdateDeviceAttributeUsecase:
        iot_platform_client = ThingsboardClientFactory.get()

        return UpdateDeviceAttributeUsecase(
            iot_platform_client=iot_platform_client,
        )

