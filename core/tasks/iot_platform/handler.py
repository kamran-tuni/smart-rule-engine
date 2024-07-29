from task_manager import app as celery_app
from core.factories.iot_platform import ExtractAllIntegrationsDeviceDataUsecaseFactory
from core.usecases.rule_engine import RuleChainExecutorUsecase

from typing import Dict

from django_tenants.utils import schema_context
from django_tenants.utils import get_tenant_model, get_public_schema_name


class ExtractAllIntegrationsDeviceDataTask(celery_app.Task):
    name = "core.tasks.iot_platform.handler.extract_all_integrations_device_data_task"

    def run(self) -> None:
        tenant_model = get_tenant_model()
        tenants = tenant_model.objects.exclude(schema_name=get_public_schema_name())

        for tenant in tenants:
            with schema_context(tenant.schema_name):
                extract_all_integrations_device_data_usecase = ExtractAllIntegrationsDeviceDataUsecaseFactory.get()
                extract_all_integrations_device_data_usecase.execute()


celery_app.register_task(ExtractAllIntegrationsDeviceDataTask())
