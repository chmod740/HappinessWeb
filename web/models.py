from django.db import models


class User(models.Model):
    phone_num = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    token = models.CharField(max_length=30)
    token = models.CharField(max_length=50)
    register_time = models.DateTimeField(auto_now=False)
    gender = models.IntegerField(default=-1)
    user_photo = models.CharField(max_length=200)
    lover = models.ForeignKey('self', null=True, blank=True)


