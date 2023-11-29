from flask import make_response
from flask_jwt_extended import get_jwt

from constants.user_type import UserType


class UserAuthentication:
    @classmethod
    def authenticate_user(cls, expected_user_type: UserType):
        jwt_payload = get_jwt()

        user_type = jwt_payload['user_type']

        if expected_user_type is None or user_type != expected_user_type.name.lower():
            return make_response("Invalid jwt token", 401)

        return None
