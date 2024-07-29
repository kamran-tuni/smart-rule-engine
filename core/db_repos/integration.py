from backend.app.models import Integration
from core.entities.integration import IntegrationEntity
from core.entities.exceptions.integration import EntityDoesNotExist

from typing import List, Optional
from datetime import datetime


class IntegrationRepo:
    def create(
        self,
        name: str,
        type: str,
        base_url: str,
        api_key: str,
        last_extraction_timestamp: datetime = None
    ) -> IntegrationEntity:
        integration = Integration.objects.create(
            name=name,
            type=type,
            base_url=base_url,
            api_key=api_key,
            last_extraction_timestamp=last_extraction_timestamp
        )

        return IntegrationEntity(
            id=integration.id,
            name=name,
            type=type,
            base_url=base_url,
            api_key=api_key
        )

    def get_by_id(self, id: int) -> IntegrationEntity:
        try:
            integration = Integration.objects.get(id=id)
        except Integration.DoesNotExist:
            raise EntityDoesNotExist

        return IntegrationEntity(
            id=integration.id,
            name=integration.name,
            type=integration.type,
            base_url=integration.base_url,
            api_key=integration.api_key,
            last_extraction_timestamp=integration.last_extraction_timestamp
        )

    def get_all_entries(self) -> List[IntegrationEntity]:
        integrations = Integration.objects.all()

        return [
            IntegrationEntity(
                id=integration.id,
                name=integration.name,
                type=integration.type,
                base_url=integration.base_url,
                api_key=integration.api_key,
                last_extraction_timestamp=integration.last_extraction_timestamp
            ) for integration in integrations
        ]

    def update(
        self, id: int,
        name: str,
        type: str,
        base_url: str,
        api_key: str,
        last_extraction_timestamp: str
    ) -> None:
        Integration.objects.filter(id=id).update(
            name=name,
            type=type,
            base_url=base_url,
            api_key=api_key,
            last_extraction_timestamp=last_extraction_timestamp
        )

    def delete_by_id(self, id: int) -> None:
        try:
            Integration.objects.get(id=id).delete()
        except Integration.DoesNotExist:
            raise EntityDoesNotExist
