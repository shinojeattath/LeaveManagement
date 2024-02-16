from django.urls import path, include
from . import views
urlpatterns = [
    path("login/",views.hr_login, name='hr_login'),
    path("homepage",views.hr_homepage,name='hr_homepage'),
    path("staff_profile_hr", views.staff_profile_hr, name='staff_profile_hr'),
    path("data_from_ajax_hr", views.data_from_ajax_hr, name='data_from_ajax_hr'),
    path("cse_departmeent",views.cs_d, name="cs_d"),
    path("eee_departmeent",views.eee_d, name="eee_d"),
    path("ece_departmeent",views.ece_d, name="ece_d"),
    path("ce_departmeent",views.ce_d, name="ce_d"),
    path("me_departmeent",views.me_d, name="me_d"),
    path("ash_departmeent",views.ash_d, name="ash_d"),
    path("departments",views.show_d, name= "show_d"), 
    path("leaverequests",views.show_l, name="show_l"),
    path('hr_leave_request',views.hr_leave_requests, name='hr_leave_request'),
    path('staff_profile_hr',views.staff_profile_hr, name='staff_profile_hr'),
    path("dutyleaves",views.duty_l, name="duty_l"),
    path("view_dutyleave",views.view_dl, name = 'view_dl'),
    path('view_requests_hr',views.view_requests_hr, name ='view_requests_hr'),
    path('leave_approval_hr',views.leave_approval_hr, name = 'leave_approval_hr'),
    path('reject_leave_hr',views.reject_leave_hr,name='reject_leave_hr')
]