# Import necessary modules and classes
from core.usecases.rule_engine import (
    RuleChainExecutorUsecase,
    AllRuleChainsExecutorUsecase,
)
from core.db_repos.rule_engine import RuleChainRepo


class RuleChainRepoFactory:
    @staticmethod
    def get() -> RuleChainRepo:
        return RuleChainRepo()


class RuleChainExecutorUsecaseFactory:
    @staticmethod
    def get() -> RuleChainExecutorUsecase:
        return RuleChainExecutorUsecase()


class AllRuleChainsExecutorUsecaseFactory:
    @staticmethod
    def get() -> AllRuleChainsExecutorUsecase:
        rule_chain_repo = RuleChainRepoFactory.get()
        rule_chain_executor_usecase = RuleChainExecutorUsecaseFactory.get()

        return AllRuleChainsExecutorUsecase(
            rule_chain_repo=rule_chain_repo,
            rule_chain_executor_usecase=rule_chain_executor_usecase
        )
