from django.contrib import admin
from .models import Staff_Details, Status_Leave_Application, Leave_Application, AlternateArrangements
# Register your models here.

admin.site.register(Staff_Details)
admin.site.register(Status_Leave_Application)
admin.site.register(Leave_Application)
admin.site.register(AlternateArrangements)