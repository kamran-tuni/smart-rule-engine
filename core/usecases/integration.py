from typing import List, Optional
from core.entities.integration import IntegrationEntity
from core.db_repos.integration import IntegrationRepo


class CreateIntegrationUseCase:
    def __init__(self, integration_repo: IntegrationRepo) -> None:
        self.integration_repo = integration_repo
        self.integration_entity: Optional[IntegrationEntity] = None
        self.integration_data: Optional[dict] = None

    def set_params(self, integration_data: dict) -> None:
        self.integration_data = integration_data
        self.integration_entity = IntegrationEntity(**self.integration_data)

    def execute(self) -> dict:
        self.integration_entity = self.integration_repo.create(
            **self.integration_entity.to_dict(exclude_fields=['id'])
        )
        return self.integration_entity.to_dict()


class UpdateIntegrationUseCase:
    def __init__(self, integration_repo: IntegrationRepo) -> None:
        self.integration_repo = integration_repo
        self.integration_entity: Optional[IntegrationEntity] = None
        self.integration_id: Optional[int] = None
        self.integration_data: Optional[dict] = None

    def set_params(self, integration_id: int, integration_data: dict) -> None:
        self.integration_id = integration_id
        self.integration_data = integration_data
        self.integration_entity = self.integration_repo.get_by_id(
            id=self.integration_id
        )
        self.integration_entity.update(**self.integration_data)
        self.integration_entity.id = integration_id

    def execute(self) -> dict:
        self.integration_repo.update(**self.integration_entity.to_dict())
        return self.integration_entity.to_dict()


class ListIntegrationUseCase:
    def __init__(self, integration_repo: IntegrationRepo) -> None:
        self.integration_repo = integration_repo
        self.integration_entities: Optional[List[IntegrationEntity]] = []

    def execute(self) -> List[dict]:
        self.integration_entities = self.integration_repo.get_all_entries()
        return [entity.to_dict() for entity in self.integration_entities]


class RetrieveIntegrationUseCase:
    def __init__(self, integration_repo: IntegrationRepo) -> None:
        self.integration_repo = integration_repo
        self.integration_entity: Optional[IntegrationEntity] = None
        self.integration_id: Optional[int] = None

    def set_params(self, integration_id: int) -> None:
        self.integration_id = integration_id

    def execute(self) -> dict:
        self.integration_entity = self.integration_repo.get_by_id(
            id=self.integration_id
        )
        return self.integration_entity.to_dict()


class DeleteIntegrationUseCase:
    def __init__(self, integration_repo: IntegrationRepo) -> None:
        self.integration_repo = integration_repo
        self.integration_id: Optional[int] = None

    def set_params(self, integration_id: int) -> None:
        self.integration_id = integration_id

    def execute(self) -> None:
        self.integration_repo.delete_by_id(id=self.integration_id)


class BulkDeleteIntegrationUseCase:
    def __init__(self, integration_repo: IntegrationRepo) -> None:
        self.integration_repo = integration_repo
        self.integration_ids: Optional[List[int]] = None

    def set_params(self, integration_ids: List[int]) -> None:
        self.integration_ids = integration_ids

    def execute(self) -> None:
        for _id in self.integration_ids:
            self.integration_repo.delete_by_id(id=_id)
