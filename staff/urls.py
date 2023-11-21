from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.homepage,name='homepage'),
    path("login/",views.user_login, name='user_login'),
    path("signup/",views.signup,name='signup'),
    path("profile/",views.profile,name='profile'),
    
]