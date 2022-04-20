
from django.db import models

# Create your models here.
class employee_details(models.Model):
    employeeid=models.IntegerField()
    employeename=models.CharField(max_length=255)
    employeeemail=models.CharField(max_length=255)
    employeecontact=models.CharField(max_length=255)
    employeedob=models.DateField()