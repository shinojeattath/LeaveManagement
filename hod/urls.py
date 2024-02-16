from django.urls import path, include
from . import views

#app_name = 'hod'

urlpatterns = [
    
    path("login/",views.hod_login, name='hod_login'),
    path("leave_request/",views.leave_request, name='leave_request'),
    path("leave_approval/",views.leave_approval, name = 'leave_approval'),
    path("send_mail",views.send_mail, name='send_mail'),
    path("reject_leave/",views.reject_leave, name = 'reject_leave'),
    path("view_request/",views.view_requests, name = 'view_request'),
    path("data_from_ajax",views.data_from_ajax, name= 'data_from_ajax'),
    path("staff_profile", views.staff_profile, name = 'staff_profile'),
    path("hod_home",views.hod_home, name='hod_home'),
    path("hod_staff",views.hod_staff, name="hod_staff"),
]