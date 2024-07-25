class ExtractDeviceDataUsecase:
    def __init__(self, iot_platform_client):
        self.iot_platform_client = iot_platform_client

    def execute(self):
        devices_data_entity = self.iot_platform_client.get_devices_data()
        return [entity.to_dict() for entity in devices_data_entity]


class UpdateDeviceAttributeUsecase:
    def __init__(self, iot_platform_client):
        self.iot_platform_client = iot_platform_client

    def set_params(self, device_id, key, value):
        self.device_id = device_id
        self.key = key
        self.value = value

    def execute(self):
        self.iot_platform_client.update_device_attribute(
            device_id=self.device_id,
            key=self.key,
            value=self.value
        )
