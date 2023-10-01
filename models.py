# habits/models.py
from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    goal = models.PositiveIntegerField()
    frequency = models.CharField(max_length=20, choices=[("daily", "Daily"), ("weekly", "Weekly"), ("monthly", "Monthly")])

class HabitRecord(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)
