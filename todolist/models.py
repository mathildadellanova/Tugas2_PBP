from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    is_finished = models.BooleanField(default=False)
