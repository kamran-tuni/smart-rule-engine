import uuid

from core.entities.iot_platform import DeviceDataEntity, DeviceParameterEntity
from core.entities.integration import IntegrationEntity
from core.entities.exceptions.iot_platform import DeviceDataAlreadyExist, EntityDoesNotExist
from backend.app.models import DeviceData, Integration


class DeviceDataRepo:
    def create(
        self,
        device_id: uuid.UUID,
        name: str,
        parameters: list,
        integration_id: int
    ) -> DeviceDataEntity:

        is_entry_exist = DeviceData.objects.filter(
            device_id=device_id,
            integration_id=integration_id
        ).exists()

        if is_entry_exist:
            raise DeviceDataAlreadyExist

        device_data = DeviceData.objects.create(
            device_id=device_id,
            name=name,
            parameters=parameters,
            integration_id=integration_id
        )

        return DeviceDataEntity(
            id=device_data.id,
            device_id=device_data.device_id,
            name=device_data.name,
            parameters=[
                DeviceParameterEntity(
                    id=param['id'],
                    name=param['name'],
                    type=param['type'],
                    unit=param['unit'],
                    extra_info=param.get('extra_info', '')
                ) for param in device_data.parameters
            ]
        )

    def update(
        self,
        id: id,
        device_id: uuid.UUID,
        name: str,
        parameters: list,
        integration_id: int
    ) -> DeviceDataEntity:

        try:
            if not id:
                entry = DeviceData.objects.filter(name=name)
            else:
                entry = DeviceData.objects.filter(id=id)
        except DeviceData.DoesNotExist:
            return EntityDoesNotExist

        entry.update(
            device_id=device_id,
            name=name,
            parameters=parameters,
            integration_id=integration_id
        )

        return DeviceDataEntity(
            id=id,
            device_id=device_id,
            name=name,
            parameters=[
                DeviceParameterEntity(
                    id=param['id'],
                    name=param['name'],
                    type=param['type'],
                    unit=param['unit'],
                    extra_info=param.get('extra_info', '')
                ) for param in parameters
            ]
        )

    def get_by_integration_id(self, integration_id: int) -> list:
        if not integration_id:
            integration_id = Integration.objects.first().id

        device_data_list = DeviceData.objects.filter(integration_id=integration_id)
        result = []

        for device_data in device_data_list:
            result.append(DeviceDataEntity(
                id=device_data.id,
                device_id=device_data.device_id,
                name=device_data.name,
                parameters=[
                    DeviceParameterEntity(
                        id=param['id'],
                        name=param['name'],
                        type=param['type'],
                        unit=param['unit'],
                        extra_info=param.get('extra_info', '')
                    ) for param in device_data.parameters
                ]
            ))

        return result
