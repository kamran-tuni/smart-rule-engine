from rest_framework.exceptions import APIException
from core.entities.exceptions import (
    integration as integration_entities_exceptions,
)


class EntityDoesNotExist(APIException):
    status_code = 404
    default_detail = 'Entity does not exist.'
    default_code = 'not_found'


integration_exception_map = {
    integration_entities_exceptions.EntityDoesNotExist: EntityDoesNotExist,
}
