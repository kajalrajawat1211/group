from django.db import models

# Create your models here.
class userLogin(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    contact=models.IntegerField(max_length=10)
    password=models.CharField(max_length=20)

class userRegister(models.Model):
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=20)


