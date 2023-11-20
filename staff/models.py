from django.db import models

# Create your models here.
class  Staff_Details(models.Model):

    employee_id = models.CharField( max_length=15, primary_key=True)
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=5)
    designation = models.CharField(max_length=20, null=True) 
    cl1_bal = models.IntegerField(null=True)
    cl2_bal = models.IntegerField(null=True)
    ML_bal = models.IntegerField(null=True)
    VL_bal  = models.IntegerField(null = True)
    DL_bal = models.IntegerField(null=True)
    LoP = models.IntegerField(null=True)
    comp_off = models.IntegerField(null = True)


class Leave_Application(models.Model):

    employee_id = models.ForeignKey(Staff_Details,on_delete=models.CASCADE, related_name="emp_id")
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=5)
    nature_of_leave = models.CharField(max_length=20)
    no_of_days = models.IntegerField(null = True)
    leave_from = models.DateField(null = False)
    reason = models.CharField(max_length=200)
    alt_class_sem = models.CharField(max_length=10)
    alt_hour = models.IntegerField(null = False)
    alt_subject = models.CharField(max_length=30)
    alt_assigned_teacher = models.CharField(max_length=20)
    alt_linways_assigned = models.CharField(max_length=5)
    status_of_request = models.CharField(max_length=10, default="PENDING")
    time_of_request = models.DateTimeField(null=True)

class Status_Leave_Application(models.Model):

    employee_id = models.ForeignKey(Staff_Details, on_delete=models.CASCADE, max_length=15, related_name='emp_id2')
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=5)
    nature_of_leave = models.CharField(max_length=20)
    no_of_days = models.IntegerField(null = True)
    leave_from = models.DateField(null = False)
    reason = models.CharField(max_length=200)
    alt_class_sem = models.CharField(max_length=10)
    alt_hour = models.IntegerField(null = False)
    alt_subject = models.CharField(max_length=30)
    alt_assigned_teacher = models.CharField(max_length=20)
    alt_linways_assigned = models.CharField(max_length=5)
    status_of_request = models.CharField(max_length=10, default="")
    time_of_request = models.DateTimeField(null=True)

