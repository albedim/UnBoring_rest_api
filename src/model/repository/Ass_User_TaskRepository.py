from src.configuration.config import sql
from src.model.entity.Ass_User_Task import Ass_User_Task


class Ass_User_TaskRepository:

    @classmethod
    def getQuantity(cls, taskId, userId=None):
        quantity = sql.session.query(Ass_User_Task).filter(Ass_User_Task.task_id == taskId)
        if userId is None:
            return len(quantity.all())
        return len(quantity.filter(Ass_User_Task.user_id == userId).all())

    @classmethod
    def create(cls, userId, taskId):
        userTask = Ass_User_Task(userId, taskId)
        sql.session.add(userTask)
        sql.session.commit()
        return userTask