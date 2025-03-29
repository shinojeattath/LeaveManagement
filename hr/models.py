from django.db import models
from staff.models import Staff_Details
# Create your models here.
class Leave_Application_hr(models.Model):

    employee_id = models.ForeignKey(Staff_Details,on_delete=models.CASCADE, related_name="emp_id4")
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=5)
    nature_of_leave = models.CharField(max_length=20)
    no_of_days = models.IntegerField(null = True)
    leave_from = models.DateField(null = False)
    reason = models.CharField(max_length=200)
    status_of_request = models.CharField(max_length=100, default="PENDING")
    time_of_request = models.DateTimeField(null=True)
    alt_linways_assigned = models.CharField(max_length=5, null=True)
    submitted = models.BooleanField(default=False)
    certificate = models.FileField(upload_to='media/')

class Medical_Certificate_Pdf(models.Model):
        employee_id = models.CharField(max_length=10, null = True)
        nature_of_leave = models.CharField(max_length=10,null = True)
        leave_id = models.IntegerField(null = True)
        pdffile = models.FileField(upload_to='medicalLeave/')
        leave_from = models.DateField(null = True)

class Duty_Leave_Certificate_Pdf(models.Model):
        employee_id = models.CharField(max_length=10, null = True)
        nature_of_leave = models.CharField(max_length=10,null = True)
        leave_id = models.IntegerField(null = True)
        pdffile = models.FileField(upload_to='dutyLeave/')
        leave_from = models.DateField(null = True)
        