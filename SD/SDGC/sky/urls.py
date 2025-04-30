# Authored by Corina Muntean, Callum Walters

from django.urls import path
# Imports the views.py
from . import views

# URL patterns for the Sky app
urlpatterns = [
    # home page
    path('', views.home, name="sky_home"),
    # the login page
    path("login", views.login_user, name="sky_login"),
    # the register page
    path("register", views.register, name="register"),
    # the logout page
    path("logout", views.logout_user, name="logout_user"),
    # the profile page
    path("profile", views.profile, name="profile"),
    # the admin login page
    path("adminLog", views.admin_login, name="admin_login"),
#--------------------------------------------------------------------------------------------------
    # By Callum Walters w1828868

    # the team summary page 
    path('teamleader_summary/', views.teamleader_summary, name="teamleader_summary"),

    # Engineer summary page
    path('engineer_summary/', views.engineer_summary, name="engineer_summary"),

    # the department leader summary page
    path('departmentleader_summary/', views.departmentleader_summary, name="departmentleader_summary"),

    # the senior manager summary page
    path('seniormanager_summary/', views.seniormanager_summary, name="seniormanager_summary"),

#-------------------------------------------------------------------------------------------------------------

]