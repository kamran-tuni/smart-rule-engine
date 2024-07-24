from task_manager import app as celery_app
from core.factories.rule_engine import AllRuleChainsExecutorUsecaseFactory
from core.usecases.rule_engine import RuleChainExecutorUsecase

from typing import Dict


class ExecuteAllRuleChainsTask(celery_app.Task):
    name = "core.tasks.rule_engine.handler.execute_all_rule_chain_task"

    def run(self, context: Dict) -> None:
        all_rule_chains_executor_use_case = AllRuleChainsExecutorUsecaseFactory.get()

        all_rule_chains_executor_use_case.set_params(
            context=context
        )
        all_rule_chains_executor_use_case.execute()


celery_app.register_task(ExecuteAllRuleChainsTask())
