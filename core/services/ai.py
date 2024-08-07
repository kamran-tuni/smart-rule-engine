import openai
from typing import Any
from settings import AI_API_KEY

# TODO: Remove this once AI is integrated
from core.tests.rule_engine.mock import (
    mocked_rule_chain,
    mocked_edit_chain,
    mocked_delete_chain
)


class AIClient:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        openai.api_key = AI_API_KEY
        return cls.instance

    @classmethod
    def clear_instance(cls):
        del cls.instance

    def send_prompt(self, messages: str) -> Any:
        # TODO: Remove this once AI is integrated
        # return mocked_rule_chain

        completion = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )
        return completion.choices[0].message.content
