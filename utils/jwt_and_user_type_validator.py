from functools import wraps
from flask_jwt_extended import jwt_required

from constants.user_type import UserType
from utils.user_authentication import UserAuthentication


def jwt_and_user_type_required(user_type: UserType):
    def decorator(func):
        @wraps(func)
        @jwt_required()
        def wrapper(*args, **kwargs):
            jwt_validation_response = UserAuthentication.authenticate_user(user_type)
            if jwt_validation_response is not None:
                return jwt_validation_response
            return func(*args, **kwargs)

        return wrapper

    return decorator
