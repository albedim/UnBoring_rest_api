import datetime
from src.configuration.config import sql
from src.utils.Utils import Utils


class User(sql.Model):
    __tablename__ = 'users'
    user_id: int = sql.Column(sql.String(14), primary_key=True, autoincrement=False)
    name: str = sql.Column(sql.String(40), nullable=True)
    instagram: str = sql.Column(sql.String(43), nullable=True)
    twitter: str = sql.Column(sql.String(43), nullable=True)
    facebook: str = sql.Column(sql.String(43), nullable=True)
    snapchat: str = sql.Column(sql.String(43), nullable=True)
    tiktok: str = sql.Column(sql.String(43), nullable=True)
    youtube: str = sql.Column(sql.String(43), nullable=True)
    telegram: str = sql.Column(sql.String(43), nullable=True)
    email: str = sql.Column(sql.String(40), nullable=False)
    password: str = sql.Column(sql.String(40), nullable=False)
    created_on: datetime.date = sql.Column(sql.Date, nullable=True)

    def __init__(self, name, email, password):
        self.user_id = Utils.createCode(14)
        self.email = email
        self.name = name
        self.password = password
        self.created_on = datetime.date.today()

    def toJSON(self, **kvargs):
        obj = {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'created_on': self.password,
            'social': [
                {
                    'name': 'instagram',
                    'url': self.instagram
                },
                {
                    'name': 'twitter',
                    'url': self.twitter
                },
                {
                    'name': 'facebook',
                    'url': self.facebook
                },
                {
                    'name': 'snapchat',
                    'url': self.snapchat
                },
                {
                    'name': 'tiktok',
                    'url': self.tiktok
                },
                {
                    'name': 'youtube',
                    'url': self.youtube
                },
                {
                    'name': 'telegram',
                    'url': self.telegram
                }
            ]
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj