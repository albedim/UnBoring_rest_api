from sqlalchemy import text
from sqlalchemy.sql.functions import random

from src.configuration.config import sql
from src.model.entity.Task import Task


class TaskRepository:

    @classmethod
    def get(cls, taskId):
        task = sql.session.query(Task).filter(Task.task_id == taskId).first()
        return task

    @classmethod
    def getAll(cls):
        tasks = sql.session.query(Task).order_by(random()).limit(5).all()
        return tasks
