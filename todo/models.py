from django.db import models
from django.utils import timezone

from user.models import UserAccount

class Todo(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    create_date = models.DateField(default=timezone.now)
    status = models.IntegerField(default=0)
    finish_date = models.DateField(default=timezone.now)

class UserTodo(models.Model):
    user_id = models.IntegerField()
    todo_id = models.IntegerField()

