from django.db import models
import mongoengine
# Create your models here.
class Employee(mongoengine.Document):
    e_id = mongoengine.IntField(required=True)
    name = mongoengine.StringField(max_length=20)
    salary = mongoengine.IntField(default=0)
    age = mongoengine.IntField(default=0)
    gender = mongoengine.StringField()
    birth = mongoengine.StringField()
    operation = mongoengine.StringField()