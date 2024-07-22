import unittest
from uuid import uuid4
from unittest import mock

from core.services.ai import AIClient
from core.usecases.rule_engine import (
    GenerateRuleChainUseCase,
)
from core.tests.rule_engine.mock import (
    mocked_rule_chain,
    mocked_rule_chain_repo_create,
)


class TestGenerateRuleChainUseCase(unittest.TestCase):
    def setUp(self):
        self.user_prompt_with_missing_info = """
            If the temperature in Room 24 is 2 degrees below the setpoint,
            turn on the heating mode and activate the heating relay for the
            HVAC system. If the temperature is 2 degrees above the setpoint,
            switch to cooling mode and activate the cooling relay. Otherwise,
            turn off both the heating and cooling relays.
        """
        self.user_prompt_with_complete_info = (
            f"{self.user_prompt_with_missing_info}."
            f"The setpoint is 73 degrees."
        )
        self.mocked_ai_response_missing_info = """
            To implement this rule, I need to know specific setpoint temperature value
            of Room 24. Could you please provide that information?
        """
        self.user_response_with_missing_info = "73"

        self.rule_chain_repo = mock.Mock()
        self.rule_chain_repo.create.side_effect = mocked_rule_chain_repo_create

    def test_execute_missing_info(self):
        ai_client = AIClient()
        use_case = GenerateRuleChainUseCase(
            ai_client=ai_client,
            rule_chain_repo=self.rule_chain_repo
        )
        ai_client.send_prompt = mock.MagicMock(return_value=self.mocked_ai_response_missing_info)

        success, response, chat_history = use_case.execute(
            user_prompt=self.user_prompt_with_missing_info
        )
        self.assertFalse(success)
        self.assertEqual(response, self.mocked_ai_response_missing_info)

        AIClient.clear_instance()

    def test_execute_provide_missing_info(self):
        ai_client = AIClient()
        use_case = GenerateRuleChainUseCase(
            ai_client=ai_client,
            rule_chain_repo=self.rule_chain_repo
        )
        ai_client.send_prompt = mock.MagicMock(side_effect=[
            self.mocked_ai_response_missing_info,
            mocked_rule_chain
        ])

        success, response, chat_history = use_case.execute(
            user_prompt=self.user_prompt_with_missing_info
        )
        self.assertFalse(success)

        success, response, chat_history = use_case.execute(
            user_prompt=self.user_response_with_missing_info,
            chat_history=chat_history
        )

        self.assertTrue(success)
        self.assertEqual(response, mocked_rule_chain)

        AIClient.clear_instance()

    def test_execute_complete_info(self):
        ai_client = AIClient()
        use_case = GenerateRuleChainUseCase(
            ai_client=ai_client,
            rule_chain_repo=self.rule_chain_repo
        )
        ai_client.send_prompt = mock.MagicMock(return_value=mocked_rule_chain)

        success, response, chat_history = use_case.execute(
            user_prompt=self.user_prompt_with_complete_info
        )
        self.assertTrue(success)
        self.assertEqual(response, mocked_rule_chain)

        AIClient.clear_instance()

    def test_execute_missing_info_with_api_call(self):
        ai_client = AIClient()
        use_case = GenerateRuleChainUseCase(
            ai_client=ai_client,
            rule_chain_repo=self.rule_chain_repo
        )

        success, response, chat_history = use_case.execute(
            user_prompt=self.user_prompt_with_missing_info
        )
        self.assertFalse(success)
        self.assertEqual(response, self.mocked_ai_response_missing_info)

        AIClient.clear_instance()


if __name__ == '__main__':
    unittest.main()
