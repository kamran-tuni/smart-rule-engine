from dataclasses import dataclass
from typing import Optional

from core.entities.base import BaseEntity


@dataclass
class IntegrationEntity(BaseEntity):
    name: str
    type: str
    base_url: str
    api_key: str
    id: Optional[int] = None
