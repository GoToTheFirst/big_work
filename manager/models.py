from django.db import models
import mongoengine
# Create your models here.


class Manager(mongoengine.Document):
    user_name = mongoengine.StringField(max_length=20)
    password = mongoengine.StringField(max_length=25)
    real_name = mongoengine.StringField(max_length=10)
    gender = mongoengine.StringField(max_length=5)

