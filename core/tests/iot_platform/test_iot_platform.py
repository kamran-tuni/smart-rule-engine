import unittest
from unittest import mock

from core.usecases.iot_platform import ExtractDeviceDataUsecase
from core.entities.iot_platform import DeviceDataEntity, DeviceParameterEntity
from core.services.iot_platform import ThingsboardClient


class TestExtractDeviceDataThingsboardUsecase(unittest.TestCase):
    def setUp(self):
        self.iot_platform_client = ThingsboardClient()
        self.usecase = ExtractDeviceDataUsecase(
            iot_platform_client=self.iot_platform_client
        )

    def test_execute(self):
        self.iot_platform_client.get_devices = mock.MagicMock(return_value=[
            {'id': {'id': '784f394c-42b6-435a-983c-b7beff2784f9', 'entityType': 'DEVICE'}, 'name': 'Device 1'},
            {'id': {'id': '2f28e056-ce22-4d6c-ae46-808d54188019', 'entityType': 'DEVICE'}, 'name': 'Device 2'}
        ])

        self.iot_platform_client.get_device_attributes = mock.MagicMock(side_effect=[
            ['active', 'latitude', 'longitude'],
            ['active', 'temperatureAlarmFlag']
        ])

        self.iot_platform_client.get_device_telemetry = mock.MagicMock(side_effect=[
            ['temperature', 'humidity'],
            ['temperature']
        ])

        result = self.usecase.execute()

        expected = [
            {
                'id': '784f394c-42b6-435a-983c-b7beff2784f9',
                'name': 'Device 1',
                'parameters': [
                    {
                        'id': 'active',
                        'name': 'active',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'latitude',
                        'name': 'latitude',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'longitude',
                        'name': 'longitude',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'temperature',
                        'name': 'temperature',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'humidity',
                        'name': 'humidity',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    }
                ]
            },

            {
                'id': '2f28e056-ce22-4d6c-ae46-808d54188019',
                'name': 'Device 2',
                'parameters': [
                    {
                        'id': 'active',
                        'name': 'active',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'temperatureAlarmFlag',
                        'name': 'temperatureAlarmFlag',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'temperature',
                        'name': 'temperature',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    }
                ]
            },
        ]
        self.assertCountEqual(result, expected)


    def test_execute_with_api_call(self):
        result = self.usecase.execute()

        expected = [
            {
                'id': '784f394c-42b6-435a-983c-b7beff2784f9',
                'name': 'Device 1',
                'parameters': [
                    {
                        'id': 'active',
                        'name': 'active',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'latitude',
                        'name': 'latitude',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'longitude',
                        'name': 'longitude',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'temperature',
                        'name': 'temperature',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'humidity',
                        'name': 'humidity',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    }
                ]
            },

            {
                'id': '2f28e056-ce22-4d6c-ae46-808d54188019',
                'name': 'Device 2',
                'parameters': [
                    {
                        'id': 'active',
                        'name': 'active',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'temperatureAlarmFlag',
                        'name': 'temperatureAlarmFlag',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                    {
                        'id': 'temperature',
                        'name': 'temperature',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    }
                ]
            },
        ]
        self.assertCountEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
