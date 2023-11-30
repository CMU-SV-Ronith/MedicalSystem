from flask import make_response
from flask_jwt_extended import get_jwt

from Response.base_response import BaseResponse
from constants.user_type import UserType
from status_codes.error_status_code import ErrorStatusCode


class UserAuthentication:
    @classmethod
    def authenticate_user(cls, expected_user_type: UserType):
        jwt_payload = get_jwt()

        user_type = jwt_payload['user_type']

        if expected_user_type is None or user_type != expected_user_type.name.lower():
            base_response = BaseResponse.from_error_code(ErrorStatusCode.INVALID_BEARER_TOKEN)
            return make_response(base_response.to_dict(), 401)

        return None
