from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.homepage,name='homepage'),
    path("login/",views.user_login, name='user_login'),
    
]