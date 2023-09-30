from datetime import timedelta
from typing import Any
from src.model.entity.User import User
from src.model.repository.Ass_User_TaskRepository import Ass_User_TaskRepository
from src.model.repository.TaskRepository import TaskRepository
from src.model.repository.UserRepository import UserRepository
from src.utils.Constants import Constants
from src.utils.Utils import Utils
from flask_jwt_extended import decode_token

from src.utils.exceptions.UserNotFoundException import UserNotFoundException


class TaskService:

    @classmethod
    def get(cls, jwt_):
        res = []

        try:
            tasks = TaskRepository.getAll()

            if jwt_ is None:

                for task in tasks:
                    quantity = Ass_User_TaskRepository.getQuantity(task.task_id)
                    res.append(task.toJSON(quantity=quantity))

                return Utils.createSuccessResponse(True, {
                    'editable': False,
                    'res': res
                })
            else:
                user = UserRepository.getUserByUserId(jwt_['user_id'])

                if user is None:
                    raise UserNotFoundException()

                for task in tasks:
                    quantity = Ass_User_TaskRepository.getQuantity(task.task_id)
                    myQuantity = Ass_User_TaskRepository.getQuantity(task.task_id, userId=user.user_id)
                    res.append(task.toJSON(quantity=quantity, my_quantity=myQuantity))

                return Utils.createSuccessResponse(True, {
                    'editable': True,
                    'res': res
                })

        except UserNotFoundException as exc:
            return Utils.createWrongResponse(False, UserNotFoundException), UserNotFoundException.code



