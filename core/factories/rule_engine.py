# Import necessary modules and classes
from core.usecases.rule_engine import (
    RuleChainExecutorUsecase,
    AllRuleChainsExecutorUsecase,
    GenerateRuleChainUseCase,
    ListRuleChainUseCase,
    RetrieveRuleChainUseCase,
    DeleteRuleChainUseCase,
    BulkDeleteRuleChainUseCase,
)
from core.factories.iot_platform import UpdateDeviceAttributeUseCaseFactory
from core.db_repos.rule_engine import RuleChainRepo
from core.services.ai import AIClient


class AIClientFactory:
    @staticmethod
    def get() -> AIClient:
        return AIClient()


class RuleChainRepoFactory:
    @staticmethod
    def get() -> RuleChainRepo:
        return RuleChainRepo()


class ListRuleChainUseCaseFactory:
    @staticmethod
    def get() -> ListRuleChainUseCase:
        rule_chain_repo = RuleChainRepo()
        return ListRuleChainUseCase(rule_chain_repo)


class RetrieveRuleChainUseCaseFactory:
    @staticmethod
    def get() -> RetrieveRuleChainUseCase:
        rule_chain_repo = RuleChainRepo()
        return RetrieveRuleChainUseCase(rule_chain_repo)


class DeleteRuleChainUseCaseFactory:
    @staticmethod
    def get() -> DeleteRuleChainUseCase:
        rule_chain_repo = RuleChainRepo()
        return DeleteRuleChainUseCase(rule_chain_repo)


class BulkDeleteRuleChainUseCaseFactory:
    @staticmethod
    def get() -> BulkDeleteRuleChainUseCase:
        rule_chain_repo = RuleChainRepo()
        return BulkDeleteRuleChainUseCase(rule_chain_repo)


class GenerateRuleChainUseCaseFactory:
    @staticmethod
    def get():
        ai_client = AIClientFactory.get()
        rule_chain_repo = RuleChainRepoFactory.get()

        return GenerateRuleChainUseCase(
            ai_client=ai_client,
            rule_chain_repo=rule_chain_repo
        )


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
