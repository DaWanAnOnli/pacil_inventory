from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    hobby = models.TextField()