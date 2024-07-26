from dataclasses import (
    asdict,
)
from typing import (
    List,
)


class BaseEntity:
    @classmethod
    def from_dict(self, data):
        return self(**data)

    def to_dict(self, exclude_fields: List[str] = []):
        _dict = asdict(self)
        for field in exclude_fields:
            _dict.pop(field)
        return _dict

    def update(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
