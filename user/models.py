from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
