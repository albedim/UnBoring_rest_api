from datetime import timedelta
from typing import Any
from flask_jwt_extended import create_access_token
from src.model.entity.User import User
from src.model.repository.Ass_User_TaskRepository import Ass_User_TaskRepository
from src.model.repository.UserRepository import UserRepository
from src.utils.Constants import Constants
from src.utils.Utils import Utils
from src.utils.exceptions.GException import GException
from src.utils.exceptions.InvalidSchemaException import InvalidSchemaException
from src.utils.exceptions.UserAlreadyExistsException import UserAlreadyExistsException
from src.utils.exceptions.UserNotFoundException import UserNotFoundException
from src.utils.schema import SCHEMA


class UserService:

    @classmethod
    def signin(cls, request):

        try:
            if not Utils.isValid(request, "USER:SIGNIN"):
                raise InvalidSchemaException()
            user = UserRepository.signin(request['email'], Utils.hash(request['password']))
            if user is None:
                raise UserNotFoundException()
            sub = {
                'user_id': user.user_id
            }
            return Utils.createSuccessResponse(True, {
                'token': create_access_token(identity=sub, expires_delta=timedelta(weeks=4))
            })
        except UserNotFoundException as exc:
            return Utils.createWrongResponse(False, UserNotFoundException), UserNotFoundException.code
        except InvalidSchemaException as exc:
            return Utils.createWrongResponse(False, InvalidSchemaException), InvalidSchemaException.code
        except Exception as exc:
            return Utils.createWrongResponse(False, GException), GException.code

    @classmethod
    def signup(cls, request):

        try:
            if not Utils.isValid(request, "USER:SIGNUP"):
                raise InvalidSchemaException()
            user = UserRepository.getUserByEmail(request['email'])
            if user is not None:
                raise UserAlreadyExistsException()
            user = UserRepository.create(request['name'], request['email'], Utils.hash(request['password']))
            sub = {
                'user_id': user.user_id
            }
            return Utils.createSuccessResponse(True, {
                'token': create_access_token(identity=sub, expires_delta=timedelta(weeks=4))
            })
        except UserAlreadyExistsException as exc:
            return Utils.createWrongResponse(False, UserAlreadyExistsException), UserAlreadyExistsException.code
        except InvalidSchemaException as exc:
            return Utils.createWrongResponse(False, InvalidSchemaException), InvalidSchemaException.code
        except Exception as exc:
            return Utils.createWrongResponse(False, GException), GException.code

    @classmethod
    def getUsersWhoPerformedAction(cls, taskId):
        try:
            users = UserRepository.getUsersWhoPerformedAction(taskId)
            res = []
            for user in users:
                res.append(user[0].toJSON(quantity=user[1]))
            return Utils.createSuccessResponse(True, res)

        except Exception as exc:
            return Utils.createWrongResponse(False, GException), GException.code
