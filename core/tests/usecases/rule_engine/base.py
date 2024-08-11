import json
from typing import List
from unittest import TestCase, mock
from core.services.ai import AIClient
from core.usecases.rule_engine import (
    GenerateRuleChainUseCase,
    RuleChainExecutorUsecase,
    AllRuleChainsExecutorUsecase,
    ListRuleChainUseCase,
    CreateRuleChainUseCase,
    UpdateRuleChainUseCase, 
    BulkDeleteRuleChainByNameUseCase
)
from core.usecases.iot_platform import UpdateDeviceAttributeUsecase
from core.services.iot_platform import ThingsboardClient
from core.db_repos.integration import IntegrationRepo
from core.tests.usecases.rule_engine.mock import (
    MOCKED_INTEGRATION_ID,
    MOCKED_AI_RESPONSE_MISSING_INFO,
    mock_rule_chain_repo_create,
    mock_rule_chain_repo_get_all_entries,
    mock_rule_chain_repo_get_by_name,
    mock_integration_repo_get_by_id,
    mock_device_data_repo_get_by_integration_id,
)

class TestBaseRuleChainUseCase(TestCase):
    def setUp(self):
        self._setup_user_prompts()
        self._setup_mocks()
        self._setup_usecases()
        self._setup_generate_rule_engine_data()

    def _setup_user_prompts(self):
        self.user_prompt_with_missing_info = (
            "If the temperature in Room 24 is 2 degrees below the setpoint, "
            "turn on the heating mode and activate the heating relay for the "
            "HVAC system. If the temperature is 2 degrees above the setpoint, "
            "switch to cooling mode and activate the cooling relay. Otherwise, "
            "turn off both the heating and cooling relays."
        )
        self.user_prompt_with_complete_info = (
            f"{self.user_prompt_with_missing_info} The setpoint is 73 degrees."
        )
        self.user_response_with_missing_info = "73"
        self.user_prompt_for_update_with_complete_info = (
            "Modify rule chain default with setpoint as 78 degrees"
        )
        self.user_prompt_for_delete = "Remove default rule chain"

    def _setup_mocks(self):
        self.ai_client = AIClient()
        self.iot_platform_client = ThingsboardClient()
        self.iot_platform_client.update_device_attribute = mock.MagicMock(
            return_value=None
        )
        self.integration_repo = mock.Mock()
        self.integration_repo.get_by_id.side_effect = mock_integration_repo_get_by_id
        self.device_data_repo = mock.Mock()
        self.device_data_repo.get_by_integration_id.side_effect = (
            mock_device_data_repo_get_by_integration_id
        )
        self.rule_chain_repo = mock.Mock()
        self.rule_chain_repo.create.side_effect = mock_rule_chain_repo_create
        self.rule_chain_repo.get_all_entries.side_effect = mock_rule_chain_repo_get_all_entries
        self.rule_chain_repo.get_by_name.side_effect = mock_rule_chain_repo_get_by_name
        self.rule_chain_repo.update.side_effect = mock.MagicMock(return_value=None)

    def _setup_usecases(self):
        self.create_rule_chain_usecase = CreateRuleChainUseCase(
            rule_chain_repo=self.rule_chain_repo
        )
        self.list_rule_chain_usecase = ListRuleChainUseCase(
            rule_chain_repo=self.rule_chain_repo
        )
        self.update_rule_chain_usecase = UpdateRuleChainUseCase(
            rule_chain_repo=self.rule_chain_repo
        )
        self.bulk_delete_rule_chain_by_name_usecase = BulkDeleteRuleChainByNameUseCase(
            rule_chain_repo=self.rule_chain_repo
        )
        self.update_device_attribute_usecase = UpdateDeviceAttributeUsecase(
            iot_platform_client=self.iot_platform_client,
            integration_repo=self.integration_repo
        )
        self.rule_chain_executor_usecase = RuleChainExecutorUsecase(
            update_device_attribute_usecase=self.update_device_attribute_usecase
        )
        self.generate_rule_engine_usecase = GenerateRuleChainUseCase(
            ai_client=self.ai_client,
            rule_chain_repo=self.rule_chain_repo,
            device_data_repo=self.device_data_repo,
            create_rule_chain_usecase=self.create_rule_chain_usecase,
            list_rule_chain_usecase=self.list_rule_chain_usecase,
            update_rule_chain_usecase=self.update_rule_chain_usecase,
            bulk_delete_rule_chain_by_name_usecase=self.bulk_delete_rule_chain_by_name_usecase,
        )
        self.all_rule_chain_executor_usecase = AllRuleChainsExecutorUsecase(
            rule_chain_repo=self.rule_chain_repo,
            rule_chain_executor_usecase=self.rule_chain_executor_usecase
        )

    def _setup_generate_rule_engine_data(self):
        self.generate_rule_engine_data_with_complete_info = {
            "user_prompt": self.user_prompt_with_complete_info,
            "chat_history": [],
            "integration_id": MOCKED_INTEGRATION_ID,
        }
        self.generate_rule_engine_data_with_missing_info = {
            "user_prompt": self.user_prompt_with_missing_info,
            "chat_history": [],
            "integration_id": MOCKED_INTEGRATION_ID,
        }
        self.generate_rule_engine_data_with_filling_missing_info = {
            "user_prompt": self.user_response_with_missing_info,
            "chat_history": [],
            "integration_id": MOCKED_INTEGRATION_ID,
        }
        self.update_rule_engine_data_with_complete_info = {
            "user_prompt": self.user_prompt_for_update_with_complete_info,
            "chat_history": [],
            "integration_id": MOCKED_INTEGRATION_ID,
        }
        self.delete_rule_engine_data = {
            "user_prompt": self.user_prompt_for_delete,
            "chat_history": [],
            "integration_id": MOCKED_INTEGRATION_ID,
        }
        self.expected_response_generate_rule_chain_with_complete_info = {
            "user_prompt": self.user_prompt_with_complete_info,
            "chat_history": [
                {
                    "role": "user",
                    "content": self.user_prompt_with_complete_info,
                },
                {
                    "role": "assistant",
                    "content": (
                        "Rule Chain is generated successfully with name default. "
                        "Refer to it with this name if need to change anything "
                        "or delete this rule chain. You can also list all the rule chains "
                        "currently in the system by asking me about it."
                    ),
                },
            ],
            "integration_id": MOCKED_INTEGRATION_ID,
            "is_generated": True,
        }
        self.expected_response_generate_rule_chain_with_missing_info = {
            "user_prompt": self.user_prompt_with_missing_info,
            "chat_history": [
                {
                    "role": "user",
                    "content": self.user_prompt_with_missing_info,
                },
                {
                    "role": "assistant",
                    "content": MOCKED_AI_RESPONSE_MISSING_INFO,
                },
            ],
            "integration_id": MOCKED_INTEGRATION_ID,
            "is_generated": False,
        }
        self.expected_response_generate_rule_chain_with_filling_missing_info = {
            "user_prompt": self.user_response_with_missing_info,
            "chat_history": [
                {
                    "role": "user",
                    "content": self.user_response_with_missing_info,
                },
                {
                    "role": "assistant",
                    "content": (
                        "Rule Chain is generated successfully with name default. "
                        "Refer to it with this name if need to change anything "
                        "or delete this rule chain. You can also list all the rule chains "
                        "currently in the system by asking me about it."
                    ),
                },
            ],
            "integration_id": MOCKED_INTEGRATION_ID,
            "is_generated": True,
        }
        self.expected_response_update_rule_chain_with_complete_info = {
            "user_prompt": self.user_prompt_for_update_with_complete_info,
            "chat_history": [
                {
                    "role": "user",
                    "content": self.user_prompt_for_update_with_complete_info,
                },
                {
                    "role": "assistant",
                    "content": (
                        "Rule Chain is updated successfully with name default. "
                        "Refer to it with this name if need to change anything "
                        "or delete this rule chain. You can also list all the rule chains "
                        "currently in the system by asking me about it."
                    ),
                },
            ],
            "integration_id": MOCKED_INTEGRATION_ID,
            "is_generated": True,
        }
        self.expected_response_delete_rule_engine = {
            "user_prompt": self.user_prompt_for_delete,
            "chat_history": [
                {
                    "role": "user",
                    "content": self.user_prompt_for_delete,
                },
                {
                    "role": "assistant",
                    "content": "Rule Chain(s) are deleted successfully.",
                },
            ],
            "integration_id": MOCKED_INTEGRATION_ID,
            "is_generated": True,
        }
