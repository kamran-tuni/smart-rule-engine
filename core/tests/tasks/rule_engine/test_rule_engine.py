import unittest
from unittest import mock

from core.tasks.rule_engine.handler import (
    ExecuteAllRuleChainsTask,
)
from core.tests.rule_engine.mock import (
    mocked_context_all_rule_chains,
)


class TestExecuteAllRuleChainsTask(unittest.TestCase):
    def setUp(self):
        pass

    def create_rule_chain(self, data):
        # TODO: Create rule chain in db
        pass

    def test_execute(self):
        execute_all_rule_chain_task = ExecuteAllRuleChainsTask()
        execute_all_rule_chain_task.run(
            context=mocked_context_all_rule_chains
        )

    def verify_action(self):
        # TODO: Verify that the action is performed
        pass
