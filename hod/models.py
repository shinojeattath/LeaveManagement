from django.db import models

# Create your models here.

class HodDetails(models.Model):
    emp_number = models.IntegerField(null = False)
    department = models.CharField(max_length=10)

