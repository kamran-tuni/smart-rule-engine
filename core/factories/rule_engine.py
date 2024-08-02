# Import necessary modules and classes
from core.usecases.rule_engine import (
    RuleChainExecutorUsecase,
    AllRuleChainsExecutorUsecase,
    GenerateRuleChainUseCase,
    CreateRuleChainUseCase,
    UpdateRuleChainUseCase,
    DeleteRuleChainUseCase,
    ListRuleChainUseCase,
    RetrieveRuleChainUseCase,
    DeleteRuleChainUseCase,
    BulkDeleteRuleChainUseCase,
)
from core.factories.iot_platform import (
    UpdateDeviceAttributeUseCaseFactory,
    DeviceDataRepoFactory,
)
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


class CreateRuleChainUseCaseFactory:
    @staticmethod
    def get() -> CreateRuleChainUseCase:
        rule_chain_repo = RuleChainRepoFactory.get()
        return CreateRuleChainUseCase(rule_chain_repo=rule_chain_repo)


class UpdateRuleChainUseCaseFactory:
    @staticmethod
    def get() -> UpdateRuleChainUseCase:
        rule_chain_repo = RuleChainRepoFactory.get()
        return UpdateRuleChainUseCase(rule_chain_repo=rule_chain_repo)


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
        device_data_repo = DeviceDataRepoFactory.get()
        create_rule_chain_usecase = CreateRuleChainUseCaseFactory.get()
        update_rule_chain_usecase = UpdateRuleChainUseCaseFactory.get()
        delete_rule_chain_usecase = DeleteRuleChainUseCaseFactory.get()

        return GenerateRuleChainUseCase(
            ai_client=ai_client,
            rule_chain_repo=rule_chain_repo,
            device_data_repo=device_data_repo,
            create_rule_chain_usecase=create_rule_chain_usecase,
            update_rule_chain_usecase=update_rule_chain_usecase,
            delete_rule_chain_usecase=delete_rule_chain_usecase
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
