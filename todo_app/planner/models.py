from django.db import models

# Create your models here.
class Task(models.Model):
    Task_name = models.CharField(max_length=250)
    priority = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return self.Task_name