from django.db import models
from django.db.models import Model



class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.IntegerField()

    def _str_(self):
        return self.name