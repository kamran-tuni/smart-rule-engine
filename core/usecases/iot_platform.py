class ExtractDeviceDataUsecase:
    def __init__(self, iot_platform_client):
        self.iot_platform_client = iot_platform_client

    def execute(self):
        devices_data_entity = self.iot_platform_client.get_devices_data()
        return [entity.to_dict() for entity in devices_data_entity]
