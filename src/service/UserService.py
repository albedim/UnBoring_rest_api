from datetime import timedelta
from typing import Any
from flask_jwt_extended import create_access_token
from src.model.entity.User import User
from src.model.repository.Ass_User_TaskRepository import Ass_User_TaskRepository
from src.model.repository.TaskRepository import TaskRepository
from src.model.repository.UserRepository import UserRepository
from src.utils.Constants import Constants
from src.utils.Utils import Utils
from src.utils.exceptions.GException import GException
from src.utils.exceptions.InvalidSchemaException import InvalidSchemaException
from src.utils.exceptions.TaskNotFoundException import TaskNotFoundException
from src.utils.exceptions.UnAuthotizedException import UnAuthorizedException
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

            for social in request['social']:
                key = social
                value = request['social'][social]
                if value != '':
                    user = cls.addSocial(user, key, value)

            UserRepository.updateUser(user)
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
            print(exc.__str__())
            return Utils.createWrongResponse(False, GException), GException.code

    @classmethod
    def getUnboredPeople(cls):
        try:
            users = UserRepository.getUnboredPeople()

            res = []

            if len(users) > 1 or (len(users) == 1 and users[0][0] is not None):
                for user in users:
                    res.append(user[0].toJSON(quantity=user[1]))

            return Utils.createSuccessResponse(True, Utils.createListOfPages(res, 4))
        except Exception as exc:
            return Utils.createWrongResponse(False, GException), GException.code

    @classmethod
    def getUsersWhoPerformedAction(cls, taskId):
        try:

            task = TaskRepository.get(taskId)

            if task is None:
                raise TaskNotFoundException()

            users = UserRepository.getUsersWhoPerformedAction(taskId)
            res = []

            if len(users) > 1 or (len(users) == 1 and users[0][0] is not None):
                for user in users:
                    res.append(user[0].toJSON(quantity=user[1], completed_on=str(user[2])))

            return Utils.createSuccessResponse(True, {
                'users': Utils.createListOfPages(res, 3),
                'task': task.toJSON()
            })

        except TaskNotFoundException as exc:
            return Utils.createWrongResponse(False, TaskNotFoundException), TaskNotFoundException.code
        except Exception as exc:
            return Utils.createWrongResponse(False, GException), GException.code

    @classmethod
    def sync(cls, authUser):
        try:
            authUserId = authUser['user_id']
            user = UserRepository.getUserByUserId(authUserId)

            if user is None:
                raise UnAuthorizedException()
            return Utils.createSuccessResponse(True, None)

        except UnAuthorizedException as exc:
            return Utils.createWrongResponse(False, UnAuthorizedException), UnAuthorizedException.code
        except Exception as exc:
            return Utils.createWrongResponse(False, GException), GException.code

    @classmethod
    def addSocial(cls, user, socialName, socialUrl):
        social = {
                'instagram': 'https://instagram.com/',
                'twitter': 'https://twitter.com/@',
                'facebook': 'https://facebook.com/people/',
                'snapchat': 'https://snapchat.com/add/',
                'tiktok': 'https://tiktok.com/@',
                'youtube': 'https://youtube.com/@',
                'telegram': 'https://t.me/'
        }
        if socialName in social:
            print(socialName, socialUrl)
            setattr(user, socialName, social[socialName] + socialUrl)
        return user

    @classmethod
    def removeSocial(cls, user, socialName):
        social = {
                'instagram': 'https://instagram.com/',
                'twitter': 'https://twitter.com/@',
                'facebook': 'https://facebook.com/people/',
                'snapchat': 'https://snapchat.com/add/',
                'tiktok': 'https://tiktok.com/@',
                'youtube': 'https://youtube.com/@',
                'telegram': 'https://t.me/'
        }
        if socialName in social:
            setattr(user, socialName, None)
        return user

    @classmethod
    def getUser(cls, userId):
        try:
            user = UserRepository.getUserByUserId(userId)

            if user is None:
                raise UserNotFoundException()

            return Utils.createSuccessResponse(True, user.toJSON())

        except UserNotFoundException as exc:
            return Utils.createWrongResponse(False, UserNotFoundException), UserNotFoundException.code
        except Exception as exc:
            return Utils.createWrongResponse(False, GException), GException.code

    @classmethod
    def updateUser(cls, userId, request):
        user = UserRepository.getUserByUserId(userId)

        if user is None:
            return UserNotFoundException()

        user.name = request['name']
        user.password = Utils.hash(request['password']) if request['password'] != "" else user.password

        for social in request['social']:
            key = social
            value = request['social'][social]
            if value != getattr(user, social):
                if value == "":
                    user = cls.removeSocial(user, key)
                else:
                    user = cls.addSocial(user, key, value)

        UserRepository.updateUser(user)
        return Utils.createSuccessResponse(True, user.toJSON())

