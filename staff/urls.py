
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.homepage,name='homepage'),
    path("login/",views.user_login, name='user_login'),
    path("signup/",views.signup,name='signup'),
    path("profile/",views.profile,name='profile'),
    path("signout/",views.signout, name = "signout"),
    path("new_leave_application/",views.new_leave_application,name='new_leave_application'),
    path("show_leave_application/",views.show_leave_application,name='show_leave_application'),
    path("new_leave_application_2",views.new_leave_application_2,name='new_leave_application_2'),
    path("new_leave_application_3",views.new_leave_application_3,name='new_leave_application_3'),
    path("upload",views.upload,name='upload'),
]