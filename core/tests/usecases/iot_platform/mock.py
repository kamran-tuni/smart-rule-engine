from core.entities.integration import IntegrationEntity
from unittest import mock

MOCK_INTEGRATION_ID = 1

MOCK_INTEGRATION_DATA = {
    "name": "demo",
    "type": "demo",
    "base_url": "demo.iot.com",
    "api_key": "123"
}


MOCK_DEVICE_DATA = [
    {
        'id': {'id': '784f394c-42b6-435a-983c-b7beff2784f9', 'entityType': 'DEVICE'},
        'name': 'Device 1'
    },
    {
        'id': {'id': '2f28e056-ce22-4d6c-ae46-808d54188019', 'entityType': 'DEVICE'},
        'name': 'Device 2'
    }
]


MOCK_DEVICE_ATTRIBUTES = [
    ['active', 'latitude', 'longitude'],
    ['active', 'temperatureAlarmFlag']
]


MOCK_DEVICE_TELEMETRY = [
    ['temperature', 'humidity'],
    ['temperature']
]


def mock_integration_repo_get_by_id(id: int) -> IntegrationEntity:
    return IntegrationEntity.from_dict(MOCK_INTEGRATION_DATA)
