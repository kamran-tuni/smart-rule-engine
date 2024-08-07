from core.services.iot_platform import IoTPlatformClient
from core.db_repos.iot_platform import DeviceDataRepo
from core.db_repos.integration import IntegrationRepo
from core.entities.iot_platform import DeviceDataEntity
from core.entities.exceptions.iot_platform import DeviceDataAlreadyExist

from datetime import datetime, timedelta
from pytz import UTC
from typing import List


class ListDeviceDataByIntegrationIdUseCase:
    def __init__(self, device_data_repo: DeviceDataRepo) -> None:
        self.device_data_repo = device_data_repo
        self.device_data_entities: Optional[List[DeviceDataEntity]] = []

    def set_params(self, integration_id: int) -> None:
        self.integration_id = integration_id

    def execute(self) -> List[dict]:
        self.device_data_entities = self.device_data_repo.get_by_integration_id(
            integration_id=self.integration_id
        )
        return [entity.to_dict() for entity in self.device_data_entities]


class ExtractDeviceDataUsecase:
    def __init__(
        self,
        device_data_repo: DeviceDataRepo,
        integration_repo: IntegrationRepo,
        iot_platform_client: IoTPlatformClient
    ):
        self.iot_platform_client = iot_platform_client
        self.device_data_repo = device_data_repo
        self.integration_repo = integration_repo
        self.integration_entity = None
        self.devices_data_entities = None
        self.integration_id = None

    def set_params(self, integration_id):
        self.integration_id = integration_id

        self.integration_entity = self.integration_repo.get_by_id(id=integration_id)

    def execute(self):
        self.iot_platform_client.set_params(
            base_url=self.integration_entity.base_url,
            api_key=self.integration_entity.api_key
        )
        self.devices_data_entities = self.iot_platform_client.get_devices_data()
        self.save_data()

    def save_data(self):
        for devices_data_entity in self.devices_data_entities:
            devices_data_entity.integration_id = self.integration_id
            try:
                self.device_data_repo.create(
                    **devices_data_entity.to_dict(exclude_fields=['id'])
                )
            except DeviceDataAlreadyExist:
                self.device_data_repo.update(
                    **devices_data_entity.to_dict()
                )


class ExtractAllIntegrationsDeviceDataUsecase:
    def __init__(
        self,
        integration_repo: IntegrationRepo,
        extract_device_data_usecase: ExtractDeviceDataUsecase
    ):
        self.integration_repo = integration_repo
        self.extract_device_data_usecase = extract_device_data_usecase
        self.integration_entity = None

    def execute(self):
        self.integration_entities = self.integration_repo.get_all_entries()
        now = datetime.utcnow().replace(tzinfo=UTC)
        try:
            for integration_entity in self.integration_entities:
                if (
                    integration_entity.last_extraction_timestamp is None or
                    (now - integration_entity.last_extraction_timestamp) >= timedelta(minutes=10)
                ):
                    self.extract_device_data_usecase.set_params(
                        integration_id=integration_entity.id
                    )
                    self.extract_device_data_usecase.execute()

                    integration_entity.last_extraction_timestamp = now
                    self.integration_repo.update(**integration_entity.to_dict())
        except Exception as e:
            print(e)


class UpdateDeviceAttributeUsecase:
    def __init__(self, iot_platform_client, integration_repo):
        self.iot_platform_client = iot_platform_client
        self.integration_repo = integration_repo

    def set_params(self, integration_id, device_id, key, value):
        self.integration_id = integration_id
        self.device_id = device_id
        self.key = key
        self.value = value

        self.integration_entity = self.integration_repo.get_by_id(id=integration_id)

    def execute(self):
        self.iot_platform_client.set_params(
            base_url=self.integration_entity.base_url,
            api_key=self.integration_entity.api_key
        )
        self.iot_platform_client.update_device_attribute(
            device_id=self.device_id,
            key=self.key,
            value=self.value
        )
