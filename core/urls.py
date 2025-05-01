# core/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Team management routes
    path('', views.list_teams, name='home'),
    path('teams/', views.list_teams, name='list_teams'),
    path('teams/add/', views.add_team, name='add_team'),
    path('teams/edit/<int:team_id>/', views.edit_team, name='edit_team'),
    path('teams/delete/<int:team_id>/', views.delete_team, name='delete_team'),

    # Authentication routes
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_teams, name='list_teams'),
    path('add/', views.add_team, name='add_team'),
    path('edit/<int:team_id>/', views.edit_team, name='edit_team'),
    path('delete/<int:team_id>/', views.delete_team, name='delete_team'),
]



