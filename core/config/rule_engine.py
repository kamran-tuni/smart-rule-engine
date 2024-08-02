system_prompt = """
    System Prompt: You will receive text inputs from an IoT Smart Rule Engine.
    Your task is to interpret the user's intentions and generate a structured JSON schema
    that mirrors the rule chain. The schema will be used to build the rule chain in the
    Rule Engine.

    Please follow the guidelines below,

    Important: In user prompt, don't assume anything and inquire the user about any missing
    information.

    Devices data:
"""

system_data = [
    {
        "id": 10,
        "name": "Room 23 Sensor",
        "parameters": [{
            "id": "temperature",
            "name": "temperature",
            "type": "float",
            "unit": "F",
            "extra_info": ""
        }]
    },
    {
        "id": 11,
        "name": "Room 24 Sensor",
        "parameters": [{
            "id": "temperature",
            "name": "Temperature",
            "type": "float",
            "unit": "F",
            "extra_info": ""
        }]
    },
    {
        "id": 12,
        "name": "Room 23 HVAC Device",
        "parameters": [{
            "id": "relay0",
            "name": "Heat Relay",
            "type": "integer",
            "unit": "",
            "extra_info": "1 -> ON, 0 -> OFF"
        },
        {
            "id": "relay1",
            "name": "Cool Relay",
            "type": "integer",
            "unit": "",
            "extra_info": "1 -> ON, 0 -> OFF"
        }]
    },
    {
        "id": 13,
        "name": "Room 24 HVAC Device",
        "parameters": [{
            "id": "relay0",
            "name": "Heat Relay",
            "type": "integer",
            "unit": "",
            "extra_info": "1 -> ON, 0 -> OFF"
        },
        {
            "id": "relay1",
            "name": "Cool Relay",
            "type": "integer",
            "unit": "",
            "extra_info": "1 -> ON, 0 -> OFF"
        }]
    }
]

expected_rule_chain = """

    Result schema. Generate unique name based on rule chain.

    {
        "name": <name>,
        "nodes": [<node>,]
    }

    Node Schema

    Generic Node Schema

    {
        "id": <id>,
        "name": <name>,
        "type": <source, script, switch, action>,
        "config": <config>,
        "target_node_id": <id>

    }

    Source Node Configuration


    {
      "device_id": <device_name>,
      "parameter_id": <parameter_name>
    }

    Script Node Configuration. Multiple inputs (input<input_no>), one output. It handles main rule chain logic. It should be JavaScript. The script should return the result.

    {

      "script": <script>

    }

    Switch Node Configuration. One input, multiple outputs. Based on the input and conditions, it enables specific output.

    [
        {
            "condition": "==",
            "value": <condition_value>,

        }
    ]

    Action Node Configuration.

    [
        {
            "device_id": <device_name>,
            "parameter_id": <parameter_name>,
            "value": <value>
        }
    ]
"""
