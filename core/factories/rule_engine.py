# Import necessary modules and classes
from core.usecases.rule_engine import (
    RuleChainExecutorUsecase,
    AllRuleChainsExecutorUsecase,
)
from core.factories.iot_platform import UpdateDeviceAttributeUseCaseFactory
from core.db_repos.rule_engine import RuleChainRepo


class RuleChainRepoFactory:
    @staticmethod
    def get() -> RuleChainRepo:
        return RuleChainRepo()


class RuleChainExecutorUsecaseFactory:
    @staticmethod
    def get() -> RuleChainExecutorUsecase:
        update_device_attribute_usecase = UpdateDeviceAttributeUseCaseFactory.get()
        return RuleChainExecutorUsecase(
            update_device_attribute_usecase=update_device_attribute_usecase
        )


class AllRuleChainsExecutorUsecaseFactory:
    @staticmethod
    def get() -> AllRuleChainsExecutorUsecase:
        rule_chain_repo = RuleChainRepoFactory.get()
        rule_chain_executor_usecase = RuleChainExecutorUsecaseFactory.get()

        return AllRuleChainsExecutorUsecase(
            rule_chain_repo=rule_chain_repo,
            rule_chain_executor_usecase=rule_chain_executor_usecase
        )
