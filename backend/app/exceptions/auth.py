from rest_framework.exceptions import APIException


class InvalidUsernameException(APIException):
    status_code = 401
    default_detail = 'Invalid username.'
    default_code = 'invalid_username'
