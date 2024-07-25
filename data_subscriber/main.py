import asyncio
import json
import setup_path
import websockets
from typing import List, Dict, Optional

from settings import IoT_PLATFORM_API_KEY, IoT_PLATFORM_BASE_URL
from core.factories.iot_platform import ExtractDeviceDataUsecaseFactory
from core.tasks.rule_engine.handler import ExecuteAllRuleChainsTask


class IoTPlatformTelemetryListener:
    def __init__(self, api_key: str, base_url: str, devices_data: List[Dict]):
        self.api_key = api_key
        self.base_url = base_url
        self.devices_data = devices_data
        self.uri = f"wss://{base_url}/api/ws/plugins/telemetry?token={api_key}"

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
                    "entityId": device["id"],
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
        print("Message received:", message)
        context = self.create_context(message=json.loads(message))
        if context:
            self.execute_rule_chains(context=context)

    def create_context(self, message: Dict) -> Optional[Dict]:
        context = {"devices": {}}
        data = message.get("data")
        if not data:
            return None
        device_id = self.devices_data[message["subscriptionId"]]["id"]
        for parameter, value in data.items():
            context["devices"][device_id] = {
                parameter: value[0][1]
            }
        return context

    def execute_rule_chains(self, context: Dict) -> None:
        execute_all_rule_chain_task = ExecuteAllRuleChainsTask()
        execute_all_rule_chain_task.delay(context=context)


class IoTPlatformDeviceExtractor:
    @staticmethod
    def extract_devices() -> List[Dict]:
        extract_device_data_usecase = ExtractDeviceDataUsecaseFactory.get()
        return extract_device_data_usecase.execute()


def main() -> None:
    devices_data = IoTPlatformDeviceExtractor.extract_devices()
    listener = IoTPlatformTelemetryListener(
        api_key=IoT_PLATFORM_API_KEY,
        base_url=IoT_PLATFORM_BASE_URL,
        devices_data=devices_data
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(listener.listen_to_all_devices_telemetry())


if __name__ == "__main__":
    main()
