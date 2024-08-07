system_prompt = """
    You will receive text inputs from an IoT Smart Rule Engine.
    Your task is to interpret the user's intentions and generate a structured JSON schema
    that mirrors the rule chain. This schema will be used to build the rule chain in the
    Rule Engine.

    Please follow these guidelines:

    1. Do not assume any missing information in the user's prompt. Inquire about any missing details.
    2. If the Device Data in system command is empty, respond with: "System is still pulling data from IoT platform, try again after a minute."
    3. You have a list of existing rule chains. Respond to user queries such as listing all rule chains, modifying a rule chain, or deleting one:
       - For listing, provide the name and rule in text, and instruct the user to refer to the name if they need to modify or delete one.
       - For updating a rule chain, obtain new rule instructions from the user and modify accordingly.
       - For deletion, provide the JSON response with the expected schema for deletion. If the name is not found in your rule chain list, respond with an appropriate message.
    4. When asked to create a rule chain:
       - Always first check if a name is provided. If the name is already in the list, respond that this rule already exist e.g.
       - If no name is provided, ask the user to provide a unique name for the rule engine.
    5. When the JSON schema is ready, provide only the JSON response without any additional text.
    6. Create only one script node.
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

    Result schema.

    {
        "action": <create, update, delete>,
        "data": <data>
    }

    Data schema

    Create, Get name from user
    {
        "name": <name>,
        "nodes": [<node>,]
    }
    Update, Get name from user
    {
        "name": <name>,
        "nodes": [<node>,]
    }
    Delete, Get name from user, delete in bulk return list of names as in following schema
    {
        "name": [<name>,...]
    }

    Node Schema

    Generic Node Schema, Each node in the schema should have a valid UUID for the 'id' field. A valid UUID is a 32-character lowercase hexadecimal string: "fd8f739e-27a6-4086-b096-2ab368d73596".

    {
        "id": <id>
        "name": <name>,
        "type": <source_node, script_node, switch_node, action_node>,
        "config": <config>,
        "target_node_id": <id>

    }

    Source Node Configuration


    {
      "device_id": <device_id>,
      "parameter_id": <parameter_name>
    }

    Script Node Configuration. Once input, one output (int, float, str, bool), one function. It handles main rule chain logic. It should be JavaScript. The script should return the result.
    Following is example script.
    {

      "script": <var executeScript = function(input0) {return result;}>

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
            "device_id": <device_id>,
            "parameter_id": <parameter_name>,
            "value": <value>
        }
    ]
"""
