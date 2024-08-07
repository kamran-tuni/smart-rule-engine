from dataclasses import dataclass
from uuid import UUID
from typing import List, Optional

from core.entities.base import BaseEntity


@dataclass
class DeviceParameterEntity(BaseEntity):
    id: str
    name: str
    type: str
    unit: str
    extra_info: str


@dataclass
class DeviceDataEntity(BaseEntity):
    device_id: UUID
    name: str
    parameters: List[DeviceParameterEntity]
    integration_id: Optional[int] = None
    id: Optional[int] = None

    def to_dict(self, exclude_fields: List[str] = []):
        data = {
            'device_id': self.device_id,
            'name': self.name,
            'parameters': [parameter.to_dict() for parameter in self.parameters],
            'integration_id': self.integration_id,
            'id': self.id
        }
        for field in exclude_fields:
            data.pop(field)

        return data
