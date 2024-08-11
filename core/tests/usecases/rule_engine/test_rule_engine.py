import json

from unittest import mock

from core.tests.usecases.rule_engine.base import TestBaseRuleChainUseCase
from core.tests.usecases.rule_engine.mock import (
    MOCKED_GENERATE_RULE_CHAIN_1,
    MOCKED_UPDATE_RULE_CHAIN,
    MOCKED_DELETE_RULE_CHAIN,
    MOCKED_AI_RESPONSE_MISSING_INFO,
    MOCKED_CONTEXT,
    MOCKED_CONTEXT_ALL_RULE_CHAINS,
    MOCKED_OUTPUT_CONTEXT,
    MOCKED_OUTPUT_CONTEXT_ALL_RULE_CHAINS,
)


class TestGenerateRuleChainUseCase(TestBaseRuleChainUseCase):
    def setUp(self):
        super().setUp()

    def test_generate_rule_with_missing_info(self):
        self.ai_client.send_prompt = mock.MagicMock(
            return_value=MOCKED_AI_RESPONSE_MISSING_INFO
        )

        self.generate_rule_engine_usecase.set_params(
            data=self.generate_rule_engine_data_with_missing_info
        )

        response = self.generate_rule_engine_usecase.execute()
        self.assertEqual(
            response, self.expected_response_generate_rule_chain_with_missing_info
        )

    def test_generate_rule_with_by_filling_missing_info(self):
        self.ai_client.send_prompt = mock.MagicMock(
            side_effect=[MOCKED_AI_RESPONSE_MISSING_INFO, json.dumps(MOCKED_GENERATE_RULE_CHAIN_1)]
        )

        self.generate_rule_engine_usecase.set_params(
            data=self.generate_rule_engine_data_with_missing_info
        )
        response = self.generate_rule_engine_usecase.execute()
        self.assertEqual(
            response, self.expected_response_generate_rule_chain_with_missing_info
        )

        self.generate_rule_engine_usecase.set_params(
            data=self.generate_rule_engine_data_with_filling_missing_info
        )
        response = self.generate_rule_engine_usecase.execute()
        self.assertEqual(
            response, self.expected_response_generate_rule_chain_with_filling_missing_info
        )

    def test_generate_rule_with_complete_info(self):
        self.ai_client.send_prompt = mock.MagicMock(return_value=json.dumps(MOCKED_GENERATE_RULE_CHAIN_1))

        self.generate_rule_engine_usecase.set_params(
            data=self.generate_rule_engine_data_with_complete_info
        )

        response = self.generate_rule_engine_usecase.execute()
        self.assertEqual(
            response, self.expected_response_generate_rule_chain_with_complete_info
        )

    def test_update_rule_with_complete_info(self):
        self.ai_client.send_prompt = mock.MagicMock(return_value=json.dumps(MOCKED_UPDATE_RULE_CHAIN))

        self.generate_rule_engine_usecase.set_params(
            data=self.update_rule_engine_data_with_complete_info
        )

        response = self.generate_rule_engine_usecase.execute()
        self.assertEqual(
            response, self.expected_response_update_rule_chain_with_complete_info
        )

    def test_delete_rule(self):
        self.ai_client.send_prompt = mock.MagicMock(return_value=json.dumps(MOCKED_DELETE_RULE_CHAIN))

        self.generate_rule_engine_usecase.set_params(
            data=self.delete_rule_engine_data
        )

        response = self.generate_rule_engine_usecase.execute()
        self.assertEqual(
            response, self.expected_response_delete_rule_engine
        )


class TestRuleChainExecutorUsecase(TestBaseRuleChainUseCase):
    def setUp(self):
        super().setUp()

        self.rule_chain_executor_usecase.set_params(
            rule_chain_data=MOCKED_GENERATE_RULE_CHAIN_1["data"],
            context=MOCKED_CONTEXT
        )

    def test_execute(self):
        response_data = self.rule_chain_executor_usecase.execute()
        self.assertEqual(response_data, MOCKED_OUTPUT_CONTEXT)


class TestAllRuleChainsExecutorUsecase(TestBaseRuleChainUseCase):
    def setUp(self):
        super().setUp()

        self.all_rule_chain_executor_usecase.set_params(
            context=MOCKED_CONTEXT_ALL_RULE_CHAINS
        )

    def test_execute(self):
        response_data = self.all_rule_chain_executor_usecase.execute()
        self.assertEqual(response_data, MOCKED_OUTPUT_CONTEXT_ALL_RULE_CHAINS)


if __name__ == '__main__':
    unittest.main()
