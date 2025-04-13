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
    path("adminLog", views.admin_login, name="admin_login")
]