import pytz
from mongoengine import *
from datetime import datetime

timezone = pytz.timezone('Asia/Saigon')


class User(Document):
    user_id = StringField(required=True, unique=True)
    user_name = StringField(required=True)
    language = StringField(required=True, default="en")


class Conversations(Document):
    sentence = StringField(required=True)
    user_id = StringField(required=True)
    mils = DateTimeField(default=datetime.utcnow())  # datetime.datetime.utcnow()
    polarity = StringField(required=True, default="neutral")
    fvs = DictField()
