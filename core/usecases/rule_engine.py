from core.services.ai import AIClient
from core.config.rule_engine import system_prompt, system_data, expected_rule_chain
from core.utils.json import get_valid_json
from core.entities.rule_engine import (
    NodeEntity,
    RuleChainEntity,
    NodeTypes
)
from core.db_repos.rule_engine import RuleChainRepo

from typing import Dict, Any, Optional, List

from py_mini_racer import py_mini_racer



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


class RuleChainExecutorUsecase:
    def __init__(self) -> None:
        pass

    def set_params(self, rule_chain_data: list, context: Dict[str, Any]):
        self.rule_chain_entity = RuleChainEntity.from_dict(rule_chain_data)
        self.nodes = {str(node.id): node for node in self.rule_chain_entity.nodes}
        self.context = context
        self.intermediate_context = {}

    def execute(self) -> dict:
        current_node_id = next(
            node_id for node_id, node in self.nodes.items()
            if node.type == NodeTypes.SOURCE_NODE
        )
        while current_node_id:
            node = self.nodes[current_node_id]
            current_node_id = self.execute_node(node)
        return self.context

    def execute_node(self, node: NodeEntity) -> Optional[str]:
        if node.type == NodeTypes.SOURCE_NODE:
            return self.execute_source_node(node)
        elif node.type == NodeTypes.SCRIPT_NODE:
            return self.execute_script_node(node)
        elif node.type == NodeTypes.SWITCH_NODE:
            return self.execute_switch_node(node)
        elif node.type == NodeTypes.ACTION_NODE:
            return self.execute_action_node(node)
        else:
            raise ValueError(f"Unknown node type: {node.type}")

    def execute_source_node(
        self,
        node: NodeEntity,
    ) -> Optional[str]:
        device_id = node.config.device_id
        parameter_id = node.config.parameter_id

        try:
            self.intermediate_context["input"] = (
                self.context["devices"][device_id][parameter_id]
            )
        except KeyError:
            return None

        return str(node.target_node_id)

    def execute_script_node(
        self,
        node: NodeEntity,
    ) -> str:
        ctx = py_mini_racer.MiniRacer()
        ctx.eval(node.config.script)
        result = ctx.call("executeScript", self.intermediate_context["input"])

        self.intermediate_context["input"] = result
        return str(node.target_node_id)

    def execute_switch_node(
        self,
        node: NodeEntity,
    ) -> Optional[str]:
        _input = self.intermediate_context["input"]
        for index, condition in enumerate(node.config):
            if condition.condition == "==" and condition.value == _input:
                return str(node.target_node_id[index])
        return None

    def execute_action_node(self, node: NodeEntity) -> Optional[str]:
        for action in node.config:
            device = self.context["devices"].setdefault(action.device_id, {})
            device[action.parameter_id] = action.value
        return None


class AllRuleChainsExecutorUsecase:
    def __init__(
        self,
        rule_chain_repo: RuleChainRepo,
        rule_chain_executor_usecase: GenerateRuleChainUseCase,
    ) -> None:
        self.rule_chain_executor_usecase = rule_chain_executor_usecase
        self.rule_chain_repo = rule_chain_repo

    def set_params(self, context: Dict[str, Any]):
        self.context = context

    def execute(self) -> List[Dict]:
        response_data = []

        rule_chain_entities = self.rule_chain_repo.get_all_entries()
        for rule_chain_entity in rule_chain_entities:
            self.rule_chain_executor_usecase.set_params(
                rule_chain_data=rule_chain_entity.to_dict(),
                context=self.context
            )
            result = self.rule_chain_executor_usecase.execute()
            response_data.append(result)
        return self.context
