import json


def get_valid_json(variable: str) -> bool:
	return json.loads(variable)
