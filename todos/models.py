from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    task = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('todo_list')
