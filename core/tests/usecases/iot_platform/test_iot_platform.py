from core.tests.usecases.iot_platform.base import TestBaseIoTPlatformUseCase
from core.tests.usecases.iot_platform.mock import (
    MOCK_INTEGRATION_ID,
)


class TestExtractDeviceDataUsecase(TestBaseIoTPlatformUseCase):

    def test_execute(self):
        self.extract_device_data_usecase.set_params(integration_id=MOCK_INTEGRATION_ID)
        self.extract_device_data_usecase.execute()

if __name__ == '__main__':
    unittest.main()
