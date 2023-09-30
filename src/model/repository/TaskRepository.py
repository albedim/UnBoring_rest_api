from sqlalchemy import text
from sqlalchemy.sql.functions import random

from src.configuration.config import sql
from src.model.entity.Task import Task


class TaskRepository:

    @classmethod
    def getAll(cls):
        tasks = sql.session.query(Task).order_by(random()).limit(5).all()
        return tasks
