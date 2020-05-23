from django.db import models

# Create your models here.

class ApplyLeave(models.Model):
    rollno = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=1000)
    status = models.CharField(max_length=30,choices=(('Approved','Approved'),('Pending','Pending'),('Rejected','Rejected')))
