import json
import re


def get_valid_json(response_text):
    try:
        # Attempt to directly parse the response text as JSON
        try:
            response_json = json.loads(response_text)
            return True, response_json
        except json.JSONDecodeError:
            pass

        json_match = re.search(r'```json([\s\S]*?)```', response_text)
        if json_match:
            json_content = json_match.group(1).strip()
            response_json = json.loads(json_content)
            return True, response_json
        else:
            raise ValueError('JSON not found in the response text')
    except (ValueError, json.JSONDecodeError) as error:
        print('Invalid JSON:', error)
        return False, None
