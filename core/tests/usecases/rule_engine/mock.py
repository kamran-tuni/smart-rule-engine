from typing import List
from core.entities.rule_engine import RuleChainEntity
from core.entities.integration import IntegrationEntity
from core.entities.iot_platform import DeviceDataEntity, DeviceParameterEntity


MOCKED_INTEGRATION_ID = 1

MOCKED_GENERATE_RULE_CHAIN_1 = {
    "action": "create",
    "data": {
        "name": "default",
        "integration_id": 1,
        "nodes": [
            {
                "id": "35a71065-8cbc-4007-bddb-28431d014e31",
                "name": "Temperature Source Room 24",
                "type": "source_node",
                "config": {
                    "device_id": "2d094910-ce67-11ed-9b15-dd2dac50548f",
                    "parameter_id": "temperature"
                },
                "target_node_id": "15f39e2c-5c7e-4847-a56d-fb157a15205d"
            },
            {
                "id": "15f39e2c-5c7e-4847-a56d-fb157a15205d",
                "name": "Temperature Script Room 24",
                "type": "script_node",
                "config": {
                    "script": "var executeScript = function(input0) {const temperature = input0;const setpoint = 73;"
                    " const delta = temperature - setpoint;let mode = 'off';if (delta <= -2) {mode = 'heat';}"
                    " else if(delta >= 2) {mode = 'cool';}return mode;}"
                },
                "target_node_id": "2840c536-45e1-4dc8-be9f-fcbfcb56857b"
            },
            {
                "id": "2840c536-45e1-4dc8-be9f-fcbfcb56857b",
                "name": "Mode Switch Room 24",
                "type": "switch_node",
                "config": [
                    {
                        "condition": "==",
                        "value": "heat"
                    },
                    {
                        "condition": "==",
                        "value": "cool"
                    },
                    {
                        "condition": "==",
                        "value": "off"
                    }
                ],
                "target_node_id": [
                    "65131c0b-851a-4412-aa3d-d9a90fb45255",
                    "2dfad79f-ec89-4a31-bc1c-ba31e1a15208",
                    "09330f01-9f53-4067-8f68-94d721553c34"
                ]
            },
            {
                "id": "65131c0b-851a-4412-aa3d-d9a90fb45255",
                "name": "Activate Heat Relay Room 24",
                "type": "action_node",
                "config": [
                    {
                        "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                        "parameter_id": "Heat Relay",
                        "value": 1
                    },
                    {
                        "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                        "parameter_id": "Cool Relay",
                        "value": 0
                    }
                ]
            },
            {
                "id": "2dfad79f-ec89-4a31-bc1c-ba31e1a15208",
                "name": "Activate Cool Relay Room 24",
                "type": "action_node",
                "config": [
                    {
                        "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                        "parameter_id": "Heat Relay",
                        "value": 0
                    },
                    {
                        "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                        "parameter_id": "Cool Relay",
                        "value": 1
                    }
              ]
            },
            {
                "id": "09330f01-9f53-4067-8f68-94d721553c34",
                "name": "Deactivate Both Relays Room 24",
                "type": "action_node",
                "config": [
                    {
                        "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                        "parameter_id": "Heat Relay",
                        "value": 0
                    },
                    {
                    "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                    "parameter_id": "Cool Relay",
                    "value": 0
                    }
                ]
            }
        ]
    }
}


MOCKED_GENERATE_RULE_CHAIN_2 = {
    "action": "create",
    "data": {
        "name": "default1",
        "integration_id": 1,
        "nodes": [
            {
                "id": "35a71065-8cbc-4007-bddb-28431d014e31",
                "name": "Temperature Source Room 23",
                "type": "source_node",
                "config": {
                    "device_id": "117ea361-51e6-47cb-be32-774d75bae642",
                    "parameter_id": "temperature"
                },
                "target_node_id": "15f39e2c-5c7e-4847-a56d-fb157a15205d"
            },
            {
                "id": "15f39e2c-5c7e-4847-a56d-fb157a15205d",
                "name": "Temperature Script Room 2",
                "type": "script_node",
                "config": {
                    "script": "var executeScript = function(input0) {const temperature = input0;const setpoint = 73;"
                    " const delta = temperature - setpoint;let mode = 'off';if (delta <= -2) {mode = 'heat';}"
                    " else if (delta >= 2) {mode = 'cool';}return mode;}"
                },
                "target_node_id": "2840c536-45e1-4dc8-be9f-fcbfcb56857b"
            },
            {
                "id": "2840c536-45e1-4dc8-be9f-fcbfcb56857b",
                "name": "Mode Switch Room 23",
                "type": "switch_node",
                "config": [
                    {
                        "condition": "==",
                        "value": "heat"
                    },
                    {
                        "condition": "==",
                        "value": "cool"
                    },
                    {
                        "condition": "==",
                        "value": "off"
                    }
                ],
                "target_node_id": [
                    "65131c0b-851a-4412-aa3d-d9a90fb45255",
                    "2dfad79f-ec89-4a31-bc1c-ba31e1a15208",
                    "09330f01-9f53-4067-8f68-94d721553c34"
                ]
            },
            {
                "id": "65131c0b-851a-4412-aa3d-d9a90fb45255",
                "name": "Activate Heat Relay Room 23",
                "type": "action_node",
                "config": [
                    {
                        "device_id": "797219af-baed-49ed-9d0f-9673a63ff607",
                        "parameter_id": "relay0",
                        "value": 1
                    },
                    {
                        "device_id": "797219af-baed-49ed-9d0f-9673a63ff607",
                        "parameter_id": "relay1",
                        "value": 0
                    }
                ]
            },
            {
                "id": "2dfad79f-ec89-4a31-bc1c-ba31e1a15208",
                "name": "Activate Cool Relay Room 23",
                "type": "action_node",
                "config": [
                    {
                        "device_id": "797219af-baed-49ed-9d0f-9673a63ff607",
                        "parameter_id": "relay0",
                        "value": 0
                    },
                    {
                        "device_id": "797219af-baed-49ed-9d0f-9673a63ff607",
                        "parameter_id": "relay1",
                        "value": 1
                    }
              ]
            },
            {
                "id": "09330f01-9f53-4067-8f68-94d721553c34",
                "name": "Deactivate Both Relays Room 23",
                "type": "action_node",
                "config": [
                    {
                        "device_id": "797219af-baed-49ed-9d0f-9673a63ff607",
                        "parameter_id": "relay0",
                        "value": 0
                    },
                    {
                    "device_id": "797219af-baed-49ed-9d0f-9673a63ff607",
                    "parameter_id": "relay1",
                    "value": 0
                    }
                ]
            }
        ]
    }
}

MOCKED_UPDATE_RULE_CHAIN = {
    "action": "update",
    "data": {
        "id": 10,
        "name": "default",
        "nodes": [
            {
                "id": "35a71065-8cbc-4007-bddb-28431d014e31",
                "name": "Temperature Source Room 29",
                "type": "source_node",
                "config": {
                    "device_id": "2d094910-ce67-11ed-9b15-dd2dac50548f",
                    "parameter_id": "temperature"
                },
                "target_node_id": "15f39e2c-5c7e-4847-a56d-fb157a15205d"
            },
            {
                "id": "15f39e2c-5c7e-4847-a56d-fb157a15205d",
                "name": "Temperature Script Room 29",
                "type": "script_node",
                "config": {
                    "script": "var executeScript = function(input0) {const temperature = input0;const setpoint = 73;const delta = temperature - setpoint;let mode = 'off';if (delta <= -2) {mode = 'heat';} else if (delta >= 2) {mode = 'cool';}return mode;}"
                },
                "target_node_id": "2840c536-45e1-4dc8-be9f-fcbfcb56857b"
            },
            {
                "id": "2840c536-45e1-4dc8-be9f-fcbfcb56857b",
                "name": "Mode Switch Room 29",
                "type": "switch_node",
                "config": [
                    {
                        "condition": "==",
                        "value": "heat"
                    },
                    {
                        "condition": "==",
                        "value": "cool"
                    },
                    {
                        "condition": "==",
                        "value": "off"
                    }
                ],
                "target_node_id": [
                    "65131c0b-851a-4412-aa3d-d9a90fb45255",
                    "2dfad79f-ec89-4a31-bc1c-ba31e1a15208",
                    "09330f01-9f53-4067-8f68-94d721553c34"
                ]
            },
            {
                "id": "65131c0b-851a-4412-aa3d-d9a90fb45255",
                "name": "Activate Heat Relay Room 29",
                "type": "action_node",
                "config": [
                    {
                        "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                        "parameter_id": "Heat Relay",
                        "value": 1
                    },
                    {
                        "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                        "parameter_id": "Cool Relay",
                        "value": 0
                    }
                ]
            },
            {
                "id": "2dfad79f-ec89-4a31-bc1c-ba31e1a15208",
                "name": "Activate Cool Relay Room 29",
                "type": "action_node",
                "config": [
                    {
                        "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                        "parameter_id": "Heat Relay",
                        "value": 0
                    },
                    {
                        "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                        "parameter_id": "Cool Relay",
                        "value": 1
                    }
              ]
            },
            {
                "id": "09330f01-9f53-4067-8f68-94d721553c34",
                "name": "Deactivate Both Relays Room 29",
                "type": "action_node",
                "config": [
                    {
                        "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                        "parameter_id": "Heat Relay",
                        "value": 0
                    },
                    {
                    "device_id": "28c69650-ce67-11ed-9b15-dd2dac50548f",
                    "parameter_id": "Cool Relay",
                    "value": 0
                    }
                ]
            }
        ]
    }
}

MOCKED_DELETE_RULE_CHAIN = {
    "action": "delete",
    "data": {
        "name": "default",
        "id": 10
    }
}


MOCKED_CONTEXT = {
    "devices": {
        "2d094910-ce67-11ed-9b15-dd2dac50548f": {"temperature": 75},
    }
}

MOCKED_OUTPUT_CONTEXT = {
    "devices": {
        "2d094910-ce67-11ed-9b15-dd2dac50548f": {"temperature": 75},
        "28c69650-ce67-11ed-9b15-dd2dac50548f": {"Heat Relay": 0, "Cool Relay": 1}
    }
}

MOCKED_CONTEXT_ALL_RULE_CHAINS = {
    "devices": {
        "2d094910-ce67-11ed-9b15-dd2dac50548f": {"temperature": 75},
        "117ea361-51e6-47cb-be32-774d75bae642": {"temperature": 71},
    }
}

MOCKED_OUTPUT_CONTEXT_ALL_RULE_CHAINS = {
    "devices": {
        "2d094910-ce67-11ed-9b15-dd2dac50548f": {"temperature": 75},
        "117ea361-51e6-47cb-be32-774d75bae642": {"temperature": 71},
        "28c69650-ce67-11ed-9b15-dd2dac50548f": {"Heat Relay": 0, "Cool Relay": 1},
        "797219af-baed-49ed-9d0f-9673a63ff607": {"relay0": 1, "relay1": 0}
    }
}


MOCKED_AI_RESPONSE_MISSING_INFO = (
    "To implement this rule, I need to know the specific setpoint "
    "temperature value of Room 24. Could you please provide that information?"
)


def mock_rule_chain_repo_create(name: str, integration_id: int, nodes: List[dict]) -> RuleChainEntity:
    return RuleChainEntity.from_dict(MOCKED_GENERATE_RULE_CHAIN_1["data"])



def mock_rule_chain_repo_get_all_entries() -> List[RuleChainEntity]:
    return [
        RuleChainEntity.from_dict(MOCKED_GENERATE_RULE_CHAIN_1["data"]),
        RuleChainEntity.from_dict(MOCKED_GENERATE_RULE_CHAIN_2["data"]),
    ]


def mock_rule_chain_repo_get_by_name(name: int) -> RuleChainEntity:
    return RuleChainEntity.from_dict(MOCKED_GENERATE_RULE_CHAIN_1["data"])


def mock_integration_repo_get_by_id(id: int) -> IntegrationEntity:
    return IntegrationEntity.from_dict({
        "name": "demo",
        "type": "demo",
        "base_url": "demo.iot.com",
        "api_key": "123"
    })


def mock_device_data_repo_get_by_integration_id(integration_id: int) -> List[DeviceDataEntity]:
    return [
        DeviceDataEntity.from_dict({
            'id': 1,
            'device_id': '784f394c-42b6-435a-983c-b7beff2784f9',
            'name': 'Device 1',
            'parameters': [
                DeviceParameterEntity.from_dict(
                    {
                        'id': 'active',
                        'name': 'active',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    }
                ),
                DeviceParameterEntity.from_dict(
                    {
                        'id': 'latitude',
                        'name': 'latitude',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    }
                ),
                DeviceParameterEntity.from_dict(
                    {
                        'id': 'longitude',
                        'name': 'longitude',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    }
                ),
                DeviceParameterEntity.from_dict(
                    {
                        'id': 'temperature',
                        'name': 'temperature',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    },
                ),
                DeviceParameterEntity.from_dict(
                    {
                        'id': 'humidity',
                        'name': 'humidity',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    }
                )
            ]
        }),
        DeviceDataEntity.from_dict({
            'id': 2,
            'device_id': '2f28e056-ce22-4d6c-ae46-808d54188019',
            'name': 'Device 2',
            'parameters': [
                DeviceParameterEntity.from_dict(
                    {
                        'id': 'active',
                        'name': 'active',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    }
                ),
                DeviceParameterEntity.from_dict(
                    {
                        'id': 'temperatureAlarmFlag',
                        'name': 'temperatureAlarmFlag',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    }
                ),
                DeviceParameterEntity.from_dict(
                    {
                        'id': 'temperature',
                        'name': 'temperature',
                        'type': '',
                        'unit': '',
                        'extra_info': ''
                    }
                )
            ]
        })
    ]
