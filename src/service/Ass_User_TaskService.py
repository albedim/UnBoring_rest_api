from datetime import timedelta
from typing import Any
from flask_jwt_extended import create_access_token
from src.model.entity.User import User
from src.model.repository.Ass_User_TaskRepository import Ass_User_TaskRepository
from src.model.repository.TaskRepository import TaskRepository
from src.utils.Constants import Constants
from src.utils.Utils import Utils
from src.utils.exceptions.GException import GException
from src.utils.exceptions.InvalidSchemaException import InvalidSchemaException
from src.utils.exceptions.TaskNotFoundException import TaskNotFoundException
from src.utils.exceptions.UnAuthotizedException import UnAuthorizedException


class Ass_User_TaskService:

    @classmethod
    def create(cls, user, request):

        try:
            if not Utils.isValid(request, "USER/TASK:CREATE"):
                raise InvalidSchemaException()

            userAuthId = user['user_id']
            if userAuthId != request['user_id']:
                raise UnAuthorizedException()

            task = TaskRepository.get(request['task_id'])
            if task is None:
                raise TaskNotFoundException()

            Ass_User_TaskRepository.create(request['user_id'], task.task_id)
            quantity = Ass_User_TaskRepository.getQuantity(task.task_id)
            my_quantity = Ass_User_TaskRepository.getQuantity(task.task_id, userId=user['user_id'])
            return Utils.createSuccessResponse(True, {
                'new': {
                    'quantity': quantity,
                    'user_quantity': my_quantity
                }
            })

        except UnAuthorizedException as exc:
            return Utils.createWrongResponse(False, UnAuthorizedException), UnAuthorizedException.code
        except TaskNotFoundException as exc:
            return Utils.createWrongResponse(False, TaskNotFoundException), TaskNotFoundException.code
        except InvalidSchemaException as exc:
            return Utils.createWrongResponse(False, InvalidSchemaException), InvalidSchemaException.code
        except Exception as exc:
            print(exc.__str__())
            return Utils.createWrongResponse(False, GException), GException.code
