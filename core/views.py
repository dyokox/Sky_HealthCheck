from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Team
from .forms import TeamForm

# Utility check
def is_admin(user):
    return user.is_superuser or user.is_staff

# ------------------- Teams -------------------
@login_required
@user_passes_test(is_admin)
def list_teams(request):
    teams = Team.objects.all()
    return render(request, 'admin/list_teams.html', {'teams': teams})

@login_required
@user_passes_test(is_admin)
def add_team(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_teams')
    return render(request, 'admin/add_team.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    form = TeamForm(request.POST or None, instance=team)
    if form.is_valid():
        form.save()
        return redirect('list_teams')
    return render(request, 'admin/edit_team.html', {'form': form, 'team': team})

@login_required
@user_passes_test(is_admin)
def delete_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        team.delete()
        return redirect('list_teams')
    return render(request, 'admin/delete_team.html', {'team': team})



