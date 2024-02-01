from django.urls import path, include
from . import views

#app_name = 'hod'

urlpatterns = [
    
    path("login/",views.hod_login, name='hod_login'),
    path("leave_request/",views.leave_request, name='leave_request'),
    path("leave_approval/",views.leave_approval, name = 'leave_approval'),
    path("send_mail",views.send_mail, name='send_mail'),
    path("reject_leave",views.reject_leave, name = 'reject_leave'),
    
]