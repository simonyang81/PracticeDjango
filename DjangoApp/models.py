from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)
    age = models.CharField(blank=True, null=True, max_length=10)
