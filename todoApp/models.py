from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    taskName = models.CharField(max_length=30)
    description = models.TextField(blank=True,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.taskName