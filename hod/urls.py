from django.urls import path, include
from . import views
urlpatterns = [
    
    path("login/",views.hod_login, name='hod_login'),
    path("leave_requests/",views.leave_requests, name = 'leave_requests'),

]