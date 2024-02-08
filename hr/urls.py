from django.urls import path, include
from . import views
urlpatterns = [
    path("login/",views.hr_login, name='hr_login'),
    path("homepage",views.hr_homepage,name='hr_homepage'),
    path("staff_profile_hr", views.staff_profile_hr, name='staff_profile_hr'),
    path("data_from_ajax_hr", views.data_from_ajax_hr, name='data_from_ajax_hr'),

]