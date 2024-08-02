system_prompt = """
    System Prompt: You will receive text inputs from an IoT Smart Rule Engine.
    Your task is to interpret the user's intentions and generate a structured JSON schema
    that mirrors the rule chain. The schema will be used to build the rule chain in the
    Rule Engine.

    Please follow the guidelines below,

    1. In user prompt, don't assume anything and inquire the user about any missing
    information.
    2. If device data is empty  then respond like System is still pulling data from
    IoT platform, try again after a minute.
    3. You are provided with list of existing rule chains, respond to user queries e.g. listing
    all rule chains, modifying a rule chain, or deleting one. In case of listing, just list the name
    along with the rule in text. Tell the user to refer with name, if need to modify or delete one.
    In case of updating a rule chain, get new rule instruction from user and modify it accordingly.
    In case of delete, provide the JSON response with expected schema for delete.


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
        "action": <create, update, delete>,
        "data": <data>
    }

    Data schema

    Create
    {
        "name": <name>,
        "nodes": [<node>,]
    }
    Update
    {
        "id": <id>,
        "name": <name>,
        "nodes": [<node>,]
    }
    Delete
    {
        "id": <id>
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
