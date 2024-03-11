from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    desc = models.TextField()
    date = models.DateField()
    remind = models.IntegerField()
    priority = models.CharField(max_length=7)
    status = models.TextField(default = 'Pending')