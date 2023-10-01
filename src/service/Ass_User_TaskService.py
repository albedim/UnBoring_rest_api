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
                return InvalidSchemaException()

            userAuthId = user['user_id']
            if userAuthId != request['user_id']:
                raise UnAuthorizedException()

            task = TaskRepository.get(request['task_id'])
            if task is None:
                return TaskNotFoundException()

            Ass_User_TaskRepository.create(request['user_id'], task.task_id)
            return Utils.createSuccessResponse(True, "Task completed! We hope you're not as bored as before now.")
        except UnAuthorizedException as exc:
            return Utils.createWrongResponse(False, UnAuthorizedException), UnAuthorizedException.code
        except TaskNotFoundException as exc:
            return Utils.createWrongResponse(False, TaskNotFoundException), TaskNotFoundException.code
        except InvalidSchemaException as exc:
            return Utils.createWrongResponse(False, InvalidSchemaException), InvalidSchemaException.code
        except Exception as exc:
            return Utils.createWrongResponse(False, GException), GException.code
