import openai
from typing import Any
from settings import AI_API_KEY


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
        completion = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )
        return completion.choices[0].message.content
