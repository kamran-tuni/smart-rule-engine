from rest_framework.exceptions import APIException
from core.entities.exceptions import (
    rule_engine as rule_engine_entities_exceptions,
)


class EntityDoesNotExist(APIException):
    status_code = 404
    default_detail = 'Entity does not exist.'
    default_code = 'not_found'


rule_engine_exception_map = {
    rule_engine_entities_exceptions.EntityDoesNotExist: EntityDoesNotExist,
}
