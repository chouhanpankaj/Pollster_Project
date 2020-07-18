from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=130)
    email = models.CharField(max_length=190)
    address = models.TextField(null=True, default=None)

