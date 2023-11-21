from django.urls import path, include
from . import views
urlpatterns = [
    
    path("login/",views.hod_login, name='hod_login'),
    
    
]