from datetime import timedelta
from typing import Any
from flask_jwt_extended import create_access_token
from src.model.entity.User import User
from src.model.repository.UserRepository import UserRepository
from src.utils.Constants import Constants
from src.utils.Utils import Utils
from src.utils.exceptions.GException import GException
from src.utils.exceptions.InvalidSchemaException import InvalidSchemaException
from src.utils.exceptions.UserNotFoundException import UserNotFoundException
from src.utils.schema import SCHEMA


class UserService:

    @classmethod
    def signin(cls, request):
        user = UserRepository.signin(request['email'], request['password'])

        try:
            if not Utils.isValid(request, "USER:SIGNIN"):
                raise InvalidSchemaException()
            if user is None:
                raise UserNotFoundException()
            sub = {
                'user_id': user.user_id
            }
            return Utils.createSuccessResponse(True, {
                'token': create_access_token(identity=sub, expires_delta=timedelta(weeks=4))
            })
        except UserNotFoundException as exc:
            return Utils.createWrongResponse(False, UserNotFoundException)
        except InvalidSchemaException as exc:
            return Utils.createWrongResponse(False, InvalidSchemaException.message
                                             .replace("{schema}", SCHEMA['USER:SIGNIN']))
        except Exception as exc:
            return Utils.createWrongResponse(False, GException)
