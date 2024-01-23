from django.urls import path, include
from . import views
urlpatterns = [
    path("login/",views.hr_login, name='hr_login'),
    path("homepage",views.hr_homepage,name='hr_homepage'),
    
]