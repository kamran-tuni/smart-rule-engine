from dataclasses import dataclass
from typing import Union, List, Optional
from uuid import UUID
from enum import Enum

from core.entities.base import BaseEntity


class NodeTypes(Enum):
    SOURCE_NODE = 'source_node'
    SCRIPT_NODE = 'script_node'
    SWITCH_NODE = 'switch_node'
    ACTION_NODE = 'action_node'


@dataclass
class SourceNodeConfigEntity(BaseEntity):
    device_id: int
    parameter_id: int


@dataclass
class ScriptNodeConfigEntity(BaseEntity):
    script: str


@dataclass
class SwitchNodeConfigEntity(BaseEntity):
    condition: str
    value: Union[int, str]


@dataclass
class ActionNodeConfigEntity(BaseEntity):
    device_id: int
    parameter_id: int
    value: Union[int, str]


@dataclass
class NodeEntity(BaseEntity):
    id: UUID
    name: str
    type: NodeTypes
    config: Union[
        SourceNodeConfigEntity,
        ScriptNodeConfigEntity,
        SwitchNodeConfigEntity,
        ActionNodeConfigEntity
    ]
    target_node_id: Union[UUID, List[UUID]]

    @classmethod
    def from_dict(cls, data: dict):
        node_type = NodeTypes(data['type'])
        config_data = data.get('config', {})
        config_class = cls.get_config_class(node_type)

        if isinstance(config_data, list):
            config = [config_class.from_dict(item) for item in config_data]
        else:
            config = config_class.from_dict(config_data)

        target_node_id = data.get('target_node_id')
        if isinstance(target_node_id, list):
            target_node_id = [UUID(item) for item in target_node_id]
        else:
            target_node_id = UUID(target_node_id) if target_node_id else None

        return cls(
            id=UUID(data['id']),
            name=data['name'],
            type=node_type,
            config=config,
            target_node_id=target_node_id
        )

    def to_dict(self) -> dict:
        data = {
            'id': str(self.id),
            'name': self.name,
            'type': self.type.value,
            'config': (
                [item.to_dict() for item in self.config]
                if isinstance(self.config, list)
                else self.config.to_dict()
            ),
            'target_node_id': (
                [str(item) for item in self.target_node_id]
                if isinstance(self.target_node_id, list)
                else (str(self.target_node_id) if self.target_node_id else None)
            )
        }
        return data

    @staticmethod
    def get_config_class(node_type: NodeTypes):
        config_classes = {
            NodeTypes.SOURCE_NODE: SourceNodeConfigEntity,
            NodeTypes.SCRIPT_NODE: ScriptNodeConfigEntity,
            NodeTypes.SWITCH_NODE: SwitchNodeConfigEntity,
            NodeTypes.ACTION_NODE: ActionNodeConfigEntity,
        }
        return config_classes[node_type]


@dataclass
class RuleChainEntity(BaseEntity):
    name: str
    nodes: List[NodeEntity]
    integration_id: int
    id: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict):
        id = data.get("id", None)
        name = data["name"]
        nodes = [NodeEntity.from_dict(node_data) for node_data in data['nodes']]
        integration_id = data["integration_id"]
        return cls(id=id, name=name, nodes=nodes, integration_id=integration_id)

    def update_from_dict(self, data: dict):
        self.id = data.get("id", self.id)
        self.name = data.get("name", self.name)
        if data.get('nodes', None):
            self.nodes = [
                NodeEntity.from_dict(node_data)
                for node_data in data.get('nodes')
            ]
        self.integration_id = data.get("integration_id", self.integration_id)

    def to_dict(self, exclude_fields: List[str] = []) -> dict:
        data = {
            'name': self.name,
            'nodes': [node.to_dict() for node in self.nodes],
            'integration_id': self.integration_id,
            'id': self.id
        }
        for field in exclude_fields:
            data.pop(field)

        return data


@dataclass
class RuleChainGenerateEntity(BaseEntity):
    user_prompt: str
    chat_history: list
    integration_id: int
    is_generated: Optional[bool] = False

