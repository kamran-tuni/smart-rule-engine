import unittest
from unittest import mock

from core.usecases.iot_platform import ExtractDeviceDataUsecase
from core.services.iot_platform import ThingsboardClient
from core.tests.usecases.iot_platform.mock import (
    MOCK_DEVICE_DATA,
    MOCK_DEVICE_ATTRIBUTES,
    MOCK_DEVICE_TELEMETRY,
    mock_integration_repo_get_by_id
)


class TestBaseIoTPlatformUseCase(unittest.TestCase):

    def setUp(self):
        self._setup_mocks()
        self._setup_usecase()

    def _setup_mocks(self):
        self.iot_platform_client = ThingsboardClient()
        self.iot_platform_client.get_devices = mock.MagicMock(return_value=MOCK_DEVICE_DATA)
        self.iot_platform_client.get_device_attributes = mock.MagicMock(
            side_effect=MOCK_DEVICE_ATTRIBUTES
        )
        self.iot_platform_client.get_device_telemetry = mock.MagicMock(
            side_effect=MOCK_DEVICE_TELEMETRY
        )

        self.integration_repo = mock.Mock()
        self.integration_repo.get_by_id.side_effect = mock_integration_repo_get_by_id

        self.device_data_repo = mock.Mock()
        self.device_data_repo.create.side_effect = mock.MagicMock(return_value=None)

    def _setup_usecase(self):
        self.extract_device_data_usecase = ExtractDeviceDataUsecase(
            iot_platform_client=self.iot_platform_client,
            integration_repo=self.integration_repo,
            device_data_repo=self.device_data_repo
        )
