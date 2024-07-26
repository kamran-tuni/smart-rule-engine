from core.db_repos.integration import IntegrationRepo
from core.usecases.integration import (
    CreateIntegrationUseCase,
    UpdateIntegrationUseCase,
    ListIntegrationUseCase,
    RetrieveIntegrationUseCase,
    DeleteIntegrationUseCase,
    BulkDeleteIntegrationUseCase
)


class IntegrationRepoFactory:
    @staticmethod
    def get() -> IntegrationRepo:
        return IntegrationRepo()


class CreateIntegrationUseCaseFactory:
    @staticmethod
    def get() -> CreateIntegrationUseCase:
        integration_repo = IntegrationRepoFactory.get()
        return CreateIntegrationUseCase(integration_repo=integration_repo)


class UpdateIntegrationUseCaseFactory:
    @staticmethod
    def get() -> UpdateIntegrationUseCase:
        integration_repo = IntegrationRepoFactory.get()
        return UpdateIntegrationUseCase(integration_repo=integration_repo)


class ListIntegrationUseCaseFactory:
    @staticmethod
    def get() -> ListIntegrationUseCase:
        integration_repo = IntegrationRepoFactory.get()
        return ListIntegrationUseCase(integration_repo=integration_repo)


class RetrieveIntegrationUseCaseFactory:
    @staticmethod
    def get() -> RetrieveIntegrationUseCase:
        integration_repo = IntegrationRepoFactory.get()
        return RetrieveIntegrationUseCase(integration_repo=integration_repo)


class DeleteIntegrationUseCaseFactory:
    @staticmethod
    def get() -> DeleteIntegrationUseCase:
        integration_repo = IntegrationRepoFactory.get()
        return DeleteIntegrationUseCase(integration_repo=integration_repo)


class BulkDeleteIntegrationUseCaseFactory:
    @staticmethod
    def get() -> BulkDeleteIntegrationUseCase:
        integration_repo = IntegrationRepoFactory.get()
        return BulkDeleteIntegrationUseCase(integration_repo=integration_repo)
