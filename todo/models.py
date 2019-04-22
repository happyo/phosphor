from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    create_date = models.DateField()
    is_done = models.BooleanField()
    finish_date = models.DateField()
