from typing import List

from core.entities.rule_engine import RuleChainEntity
from core.entities.exceptions.rule_engine import EntityDoesNotExist
from backend.app.models import RuleChain, Integration


class RuleChainRepo:
    def __init__(self) -> None:
        pass

    def create(
        self,
        name: str,
        nodes: List,
        integration_id: int
    ) -> RuleChainEntity:

        if not integration_id:
            integration_id = Integration.objects.first().id
        rule_chain = RuleChain.objects.create(
            name=name,
            nodes=nodes,
            integration_id=integration_id
        )

        return RuleChainEntity.from_dict({
            'id': rule_chain.id,
            'integration_id': integration_id,
            'name': name,
            'nodes': nodes
        })

    def get_all_entries(self) -> List[RuleChainEntity]:
        rule_chains = RuleChain.objects.all()

        return [
            RuleChainEntity.from_dict({
                'id': rule_chain.id,
                'name': rule_chain.name,
                'nodes': rule_chain.nodes,
                'integration_id': rule_chain.integration.id
            }) for rule_chain in rule_chains
        ]

    def get_by_id(self, id: int) -> RuleChainEntity:
        try:
            rule_chain = RuleChain.objects.get(id=id)
        except RuleChain.DoesNotExist:
            raise EntityDoesNotExist

        return RuleChainEntity.from_dict({
            'id': rule_chain.id,
            'integration_id': rule_chain.integration.id,
            'name': rule_chain.name,
            'nodes': rule_chain.nodes
        })

    def update(
        self,
        id: int,
        name: str,
        nodes: List,
        integration_id: int
    ) -> RuleChainEntity:
        RuleChain.objects.filter(id=id).update(
            name=name,
            nodes=nodes,
            integration_id=rule_chain.integration.id,
        )

        return RuleChainEntity.from_dict({
            'id': id,
            'name': name,
            'nodes': nodes,
            'integration_id': integration.id,
        })

    def delete_by_id(self, id: int):
        try:
            rule_chain = RuleChain.objects.get(id=id).delete()
        except RuleChain.DoesNotExist:
            raise EntityDoesNotExist
