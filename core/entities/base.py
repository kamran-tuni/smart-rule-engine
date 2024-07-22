from dataclasses import asdict


class BaseEntity:
    @classmethod
    def from_dict(self, data: dict):
        return self(**data)

    def to_dict(self) -> dict:
        return asdict(self)
