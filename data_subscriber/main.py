import asyncio
import json
import setup_path
import websockets
from typing import List, Dict, Optional

from core.factories.iot_platform import ListDeviceDataByIntegrationIdUseCaseFactory
from core.factories.integration import ListIntegrationUseCaseFactory
from core.tasks.rule_engine.handler import ExecuteAllRuleChainsTask

from django_tenants.utils import get_tenant_model, get_public_schema_name
from django_tenants.utils import schema_context

from asgiref.sync import sync_to_async


class IoTPlatformTelemetryListener:
    def __init__(self, api_key: str, base_url: str, devices_data: List[Dict], tenant: str):
        self.api_key = api_key
        self.base_url = base_url
        self.devices_data = devices_data
        self.uri = f"wss://{base_url}/api/ws/plugins/telemetry?token={api_key}"
        self.tenant = tenant

    async def listen_to_all_devices_telemetry(self) -> None:
        async with websockets.connect(self.uri) as websocket:
            for index, device in enumerate(self.devices_data):
                await self.subscribe_to_device_telemetry(websocket, device, index)

            try:
                async for message in websocket:
                    await self.handle_message(message)
            except websockets.ConnectionClosed:
                print("Connection closed, retrying...")
                await asyncio.sleep(5)
                await self.listen_to_all_devices_telemetry()

    async def subscribe_to_device_telemetry(self, websocket, device: Dict, index: int) -> None:
        subscribe_object = {
            "tsSubCmds": [
                {
                    "entityType": "DEVICE",
                    "entityId": str(device["device_id"]),
                    "scope": "LATEST_TELEMETRY",
                    "cmdId": index
                }
            ],
            "historyCmds": [],
            "attrSubCmds": []
        }
        await websocket.send(json.dumps(subscribe_object))
        print("Subscription message sent:", json.dumps(subscribe_object))

    async def handle_message(self, message: str) -> None:
        context = self.create_context(message=json.loads(message))
        if context:
            self.execute_rule_chains(context=context)

    def create_context(self, message: Dict) -> Optional[Dict]:
        context = {"devices": {}}
        data = message.get("data")
        if not data:
            return None

        device_id = str(self.devices_data[message["subscriptionId"]]["device_id"])
        for parameter, value in data.items():
            context["devices"][device_id] = {
                parameter: value[0][1]
            }
        return context

    def execute_rule_chains(self, context: Dict) -> None:
        execute_all_rule_chain_task = ExecuteAllRuleChainsTask()
        execute_all_rule_chain_task.delay(tenant=self.tenant, context=context)




async def manage_tenant_subscriptions(tenant) -> None:
    with schema_context(tenant):
        tasks = []
        integrations = await get_all_integrations(tenant=tenant)
        for integration in integrations:
            devices_data = await get_all_devices(
                tenant=tenant,
                integration_id=integration["id"]
            )

            listener = IoTPlatformTelemetryListener(
                tenant=tenant,
                api_key=integration["api_key"],
                base_url=integration["base_url"],
                devices_data=devices_data
            )
            tasks.append(await listener.listen_to_all_devices_telemetry())

        await tasks


@sync_to_async
def get_all_devices(tenant, integration_id: int) -> List[Dict]:
    with schema_context(tenant):
        list_device_data_by_integration_id_usecase = ListDeviceDataByIntegrationIdUseCaseFactory.get()
        list_device_data_by_integration_id_usecase.set_params(integration_id=integration_id)
        return list_device_data_by_integration_id_usecase.execute()


@sync_to_async
def get_all_integrations(tenant) -> List[Dict]:
    with schema_context(tenant):
        list_integration_use_case = ListIntegrationUseCaseFactory.get()
        integrations = list_integration_use_case.execute()
        return integrations


async def main() -> None:
    tenant_model = get_tenant_model()
    tenants = await sync_to_async(list)(
        tenant_model.objects.exclude(schema_name=get_public_schema_name())
    )

    tasks = []
    for tenant in tenants:
        tasks.append(manage_tenant_subscriptions(tenant=tenant.schema_name))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
