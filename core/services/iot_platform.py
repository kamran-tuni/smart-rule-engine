import os
import requests

from abc import ABC, abstractmethod
from settings import IoT_PLATFORM_API_KEY, IoT_PLATFORM_BASE_URL
from core.entities.iot_platform import DeviceParameterEntity, DeviceDataEntity


class IoTPlatformClient(ABC):
    def __init__(self):
        self.api_key = IoT_PLATFORM_API_KEY
        self.base_url = IoT_PLATFORM_BASE_URL

    @abstractmethod
    def get_devices(self, page_size, page):
        pass

    @abstractmethod
    def get_device_attributes(self, device_id):
        pass

    @abstractmethod
    def get_device_telemetry(self, device_id):
        pass

    @abstractmethod
    def transform_device_data(self, device_id):
        pass


class ThingsboardClient(IoTPlatformClient):
    def _get_headers(self):
        return {'X-Authorization': f'Bearer {self.api_key}'}

    def get_devices(self, page_size=100, page=0):
        url = f'https://{self.base_url}/api/tenant/deviceInfos?pageSize={page_size}&page={page}'
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()['data']

    def get_device_attributes(self, device_id):
        url = f'https://{self.base_url}/api/plugins/telemetry/DEVICE/{device_id}/keys/attributes'
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_device_telemetry(self, device_id):
        url = f'https://{self.base_url}/api/plugins/telemetry/DEVICE/{device_id}/keys/timeseries'
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_devices_data(self):
        devices_data = []
        devices = self.get_devices()

        for device in devices:
            device_data = self.transform_device_data(device)
            devices_data.append(device_data)

        return devices_data

    def transform_device_data(self, device):
        device_id = device['id']['id']
        attributes = self.get_device_attributes(device_id)
        telemetry = self.get_device_telemetry(device_id)

        parameters = [
            DeviceParameterEntity(
                attr,
                attr,
                '',
                '',
                ''
            ) for attr in attributes
        ] + [
            DeviceParameterEntity(
                tele,
                tele,
                '',
                '',
                ''
            ) for tele in telemetry
        ]

        return DeviceDataEntity(device_id, device['name'], parameters)
