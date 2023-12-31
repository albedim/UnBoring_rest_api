import datetime
from src.configuration.config import sql
from src.utils.Utils import Utils


class Task(sql.Model):
    __tablename__ = 'tasks'
    task_id: str = sql.Column(sql.String(14), autoincrement=False, primary_key=True)
    name: str = sql.Column(sql.String(40), nullable=True)
    reported: int = sql.Column(sql.Integer, nullable=False)
    created_on: datetime.date = sql.Column(sql.Date, nullable=True)

    def __init__(self, name):
        self.task_id = Utils.createCode(14)
        self.name = name
        self.reported = 0
        self.created_on = datetime.date.today()

    def toJSON(self, **kvargs):
        obj = {
            'task_id': self.task_id,
            'name': self.name,
            'reported': self.reported,
            'created_on': str(self.created_on)
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj