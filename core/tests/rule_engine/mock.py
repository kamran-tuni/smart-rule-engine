from core.entities.rule_engine import RuleChainEntity
from typing import List
import json


mocked_rule_chain = """{
    "name": "default",
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
                "script": "var executeScript = function(input0) {const temperature = input0;const setpoint = 73;const delta = temperature - setpoint;let mode = 'off';if (delta <= -2) {mode = 'heat';} else if (delta >= 2) {mode = 'cool';}return mode;}"
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
"""

mocked_rule_chain_1 = """{
    "nodes": [
        {
            "id": "35a71065-8cbc-4007-bddb-28431d014e31",
            "name": "Temperature Source Room 23",
            "type": "source_node",
            "config": {
                "device_id": 10,
                "parameter_id": "temperature"
            },
            "target_node_id": "15f39e2c-5c7e-4847-a56d-fb157a15205d"
        },
        {
            "id": "15f39e2c-5c7e-4847-a56d-fb157a15205d",
            "name": "Temperature Script Room 2",
            "type": "script_node",
            "config": {
                "script": "var executeScript = function(input0) {const temperature = input0;const setpoint = 73;const delta = temperature - setpoint;let mode = 'off';if (delta <= -2) {mode = 'heat';} else if (delta >= 2) {mode = 'cool';}return mode;}"
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
                    "device_id": 15,
                    "parameter_id": "relay0",
                    "value": 1
                },
                {
                    "device_id": 15,
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
                    "device_id": 15,
                    "parameter_id": "relay0",
                    "value": 0
                },
                {
                    "device_id": 15,
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
                    "device_id": 15,
                    "parameter_id": "relay0",
                    "value": 0
                },
                {
                "device_id": 15,
                "parameter_id": "relay1",
                "value": 0
                }
            ]
        }
    ]
}
"""

def mocked_rule_chain_repo_create(
    nodes: list,
) -> RuleChainEntity:
    return


mocked_context = {
    "devices": {
        11: {"temperature": 75},
    }
}

mocked_output_context = {
    "devices": {
        11: {"temperature": 75},
        13: {"relay0": 0, "relay1": 1}
    }
}

mocked_context_all_rule_chains = {
    "devices": {
        11: {"temperature": 75},
        10: {"temperature": 71},
    }
}

mocked_output_context_all_rule_chains = {
    "devices": {
        11: {"temperature": 75},
        10: {"temperature": 71},
        13: {"relay0": 0, "relay1": 1},
        15: {"relay0": 1, "relay1": 0}
    }
}


def mocked_rule_chain_repo_get_all_entries() -> List[RuleChainEntity]:
    return [
        RuleChainEntity.from_dict(json.loads(mocked_rule_chain)),
        RuleChainEntity.from_dict(json.loads(mocked_rule_chain_1))
    ]
