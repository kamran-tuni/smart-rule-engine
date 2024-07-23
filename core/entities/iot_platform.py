from dataclasses import dataclass
from uuid import UUID
from typing import List

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
    id: UUID
    name: str
    parameters: List[DeviceParameterEntity]

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'parameters': [parameter.to_dict() for parameter in self.parameters]
        }
