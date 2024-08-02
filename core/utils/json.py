import json


def get_valid_json(variable: str) -> bool:
    try:
        return True, json.loads(variable)
    except Exception:
        return False, {}
