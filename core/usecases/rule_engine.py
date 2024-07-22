from core.services.ai import AIClient
from core.config.rule_engine import system_prompt, system_data, expected_rule_chain
from core.utils.json import get_valid_json
from core.entities.rule_engine import RuleChainEntity
from core.db_repos.rule_engine import RuleChainRepo


class GenerateRuleChainUseCase:
    def __init__(self, ai_client: AIClient, rule_chain_repo: RuleChainRepo):
        self.ai_client = ai_client
        self.rule_chain_repo = rule_chain_repo
        self.rule_chain_entity = None

    def execute(self, user_prompt: str, chat_history: list = []):
        result = False

        if not chat_history:
            messages = [
                {"role": "system", "content": f"{system_prompt}{system_data}{expected_rule_chain}"},
                {"role": "user", "content": user_prompt}
            ]
        else:
            messages = chat_history + [{"role": "user", "content": user_prompt}]

        response = self.ai_client.send_prompt(
            messages=messages
        )

        try:
            response_data = get_valid_json(response)
            result = True
            self.rule_chain_entity = RuleChainEntity.from_dict(response_data)

            # TODO: Use the entity to perform any buisness logic

            self.save_rule_chain()

            # TODO: Store the rule chain in db through db repo

            chat_history = messages + [{"role": "assistant", "content": "Rule Chain is generated successfully!"}]
        except Exception:
            chat_history = messages + [{"role": "assistant", "content": response}]

        return result, response, chat_history


    def save_rule_chain(self):
        self.rule_chain_repo.create(
            **self.rule_chain_entity.to_dict()
        )
