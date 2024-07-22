from core.entities.rule_engine import RuleChainEntity


mocked_rule_chain = """{
    "nodes": [
        {
            "id": "35a71065-8cbc-4007-bddb-28431d014e31",
            "name": "Temperature Source Room 24",
            "type": "source_node",
            "config": {
                "device_id": 11,
                "parameter_id": "temperature"
            },
            "target_node_id": "15f39e2c-5c7e-4847-a56d-fb157a15205d"
        },
        {
            "id": "15f39e2c-5c7e-4847-a56d-fb157a15205d",
            "name": "Temperature Script Room 24",
            "type": "script_node",
            "config": {
                "script": "const temperature = input0;const setpoint = 73;const delta = temperature - setpoint;let mode = 'off';if (delta < -2) {mode = 'heat';} else if (delta > 2) {mode = 'cool';}return mode;"
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
            "target_node_ids": {
                "0": "65131c0b-851a-4412-aa3d-d9a90fb45255",
                "1": "2dfad79f-ec89-4a31-bc1c-ba31e1a15208",
                "2": "09330f01-9f53-4067-8f68-94d721553c34"
            }
        },
        {
            "id": "65131c0b-851a-4412-aa3d-d9a90fb45255",
            "name": "Activate Heat Relay Room 24",
            "type": "action_node",
            "config": [
                {
                    "device_id": 13,
                    "parameter_id": "relay0",
                    "value": 1
                },
                {
                    "device_id": 13,
                    "parameter_id": "relay1",
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
                    "device_id": 13,
                    "parameter_id": "relay0",
                    "value": 0
                },
                {
                    "device_id": 13,
                    "parameter_id": "relay1",
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
                    "device_id": 13,
                    "parameter_id": "relay0",
                    "value": 0
                },
                {
                "device_id": 13,
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
