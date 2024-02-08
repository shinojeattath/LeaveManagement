from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Staff_Details(models.Model):

    employee_id = models.CharField( max_length=15, primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=5)
    designation = models.CharField(max_length=20, null=True) 
    cl1_bal = models.PositiveIntegerField(null=True)
    cl2_bal = models.PositiveIntegerField(null=True)
    ML_bal = models.PositiveIntegerField(null=True)
    VL_bal  = models.PositiveIntegerField(null = True)
    DL_bal = models.PositiveIntegerField(null=True)
    LoP = models.PositiveIntegerField(null=True)
    comp_off = models.PositiveBigIntegerField(null = True)

    def __str__(self):
        return str(self.employee_id)

class Leave_Application(models.Model):

    employee_id = models.ForeignKey(Staff_Details,on_delete=models.CASCADE, related_name="emp_id")
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=5)
    nature_of_leave = models.CharField(max_length=20)
    no_of_days = models.IntegerField(null = True)
    leave_from = models.DateField(null = False)
    reason = models.CharField(max_length=200)
    status_of_request = models.CharField(max_length=10, default="PENDING")
    time_of_request = models.DateTimeField(null=True)
    alt_linways_assigned = models.CharField(max_length=5, null=True)


class AlternateArrangements(models.Model):
    #time_of_request = models.DateTimeField(null=True)
    employee_id = models.ForeignKey(Staff_Details,on_delete=models.CASCADE, related_name="emp_id3")
    alt_class = models.CharField(max_length=10, null = True)
    alt_semester = models.CharField(max_length = 5, null = True)
    alt_hour = models.IntegerField(null = False)
    #alt_subject = models.CharField(max_length=30)
    alt_assigned_teacher = models.CharField(max_length=20)
    #alt_linways_assigned = models.CharField(max_length=5)

    def __str__(self):
        return str(self.employee_id)
    
class Status_Leave_Application(models.Model):

    employee_id = models.ForeignKey(Staff_Details, on_delete=models.CASCADE, max_length=15, related_name='emp_id2')
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=5)
    nature_of_leave = models.CharField(max_length=20)
    no_of_days = models.IntegerField(null = True)
    leave_from = models.DateField(null = False)
    reason = models.CharField(max_length=200)
    alt_class_sem = models.CharField(max_length=10)
    alt_hour = models.IntegerField(null = True)
    alt_subject = models.CharField(max_length=30, null = True)
    alt_assigned_teacher = models.CharField(max_length=20)
    alt_linways_assigned = models.CharField(max_length=5, null = True)
    status_of_request = models.CharField(max_length=10, default="")
    time_of_request = models.DateTimeField(null=True)

