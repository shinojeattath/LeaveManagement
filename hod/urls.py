from django.urls import path, include
from . import views
urlpatterns = [
    
    path("login/",views.hod_login, name='hod_login'),
    path("leave_request/",views.leave_request, name='leave_request')
    
    
]