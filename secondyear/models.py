from django.db import models

# Create your models here.


class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phno = models.IntegerField()

class Attend(models.Model):
    date = models.CharField(max_length=100)
    rollno = models.IntegerField()
    status = models.BooleanField(default=False)

