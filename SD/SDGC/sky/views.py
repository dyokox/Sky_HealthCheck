# Authored by Corina Muntean, Callum Walters, Shushanik Hayrapetyan

from django.shortcuts import render, redirect
# Hashes passwords, making it secure
from django.contrib.auth.hashers import make_password
# Allows to display messages to user e.g. failed or successful login attempt
from django.contrib import messages
# Importing the login decorator, user can access certain pages
# Only if they are logged in
from django.contrib.auth.decorators import login_required
# Importing the custom user registration form
from .forms import CreateUserForm
# Built in auth, login and logout from Django
from django.contrib.auth import authenticate, login, logout
# Importing the custom decorator preventing logged users to access 
# certain pages
from .decorators import logout_required
from .models import Card, Session, Vote
from .forms import VoteFormSet


# View for the home pagee
def home(request):
    return render(request, 'sky/home.html')


# ----------------------------------------------------------------------------------------------------------
# By Corina Muntean // w1993775

# Only logout users can access a login page
@logout_required
def login_user(request):
        # Checks the method of the form
        if request.method == "POST":
            # Retrieves username from form
            username = request.POST.get("username")
            # Retrieves password from form
            password = request.POST.get("password")

            # Authenticates the user with Django's built in function
            user = authenticate(request, username=username, password=password)

            # Checks the credentials
            if user is not None:
                # Logs the user in if they are
                login(request, user)
                # Greets the user for a visual confirmation
                messages.success(request, f"Welcome back, {user.username}!")
                # Redirects the user to home page
                return redirect('sky_home')
            # If credentials are not valid
            else:  
                # Notifies the user that username or password is not valid
                messages.error(request, "Invalid username and/or password.")
        # Renders the page
        return render(request, 'sky/login.html')

# User can only access register.html if they are logged out
@logout_required
def register(request):
    # Checks the method of the form
    if request.method == "POST":
        # Create the form instance with the form data
        form = CreateUserForm(request.POST)
        # If the form is valid
        if form.is_valid():
            # Doesn;t save the data yet
            user = form.save(commit=False)
            # Because we want to hash the password for security
            user.password = make_password(form.cleaned_data['password'])

            # Explicitly set normal user permissions
            # Cannot access admin panel
            user.is_staff = False
            # No superuser powers
            user.is_superuser = False 

            # Saves the user information
            user.save()
            # Visual confirmation that the account was created
            messages.success(request, "Account created successfully!")
            # Redirects the user to the login page
            return redirect('sky_login')
        # Tells the user to correct their mistakes
        else:
            messages.error(request, "Please correct the errors.")
    # Form method is GET
    else:
        form = CreateUserForm()

    # Renders the page
    return render(request, 'sky/register.html', {'form': form})

# User can access this only if they are logged in
@login_required(login_url='sky_login')
def logout_user(request):
    # Logs out the user, using a built-in Django function
    logout(request)
    # Visual confirmation that the user was logged out
    messages.success(request, "You have been logged out successfully.")
    # Redirect to login page after logout
    return redirect('sky_login')

# User can access the profile.html only logged
@login_required(login_url='sky_login')
def profile(request):
    # Checks the method used by the form
    if request.method == "POST":
        # The currently logged-in user
        user = request.user

        # Only update fields if user entered new data
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Updates the data in db
        if fullname:
            user.fullname = fullname
        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password = make_password(password)

        # Saves the data to db
        user.save()
        # Visual confirmation that the profile was updated
        messages.success(request, "Profile updated successfully!")
        # Reload the profile page after save
        return redirect('profile')
    # Renders the page
    return render(request, 'sky/profile.html')

# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------
    # By Callum Walters w1828868

    # View for Team Leader to see overall team summary
@login_required(login_url='sky_login')
def teamleader_summary(request):
    # The currently logged-in user
    user = request.user

    # Checks if user has the correct role
    if not hasattr(user, 'role') or user.role.strip().lower() != "team leader":
        messages.error(request, "You do not have permission to view this page.")
        return redirect('sky_home')

    return render(request, 'sky/teamLeaderSummary.html')


@login_required(login_url='sky_login')
def engineer_summary(request):
    # The currently logged-in user
    user = request.user

    # Checks if user is an Engineer
    if not hasattr(user, 'role') or user.role.strip().lower() != "engineer":
        messages.error(request, "You do not have permission to view this page.")
        return redirect('sky_home')

    return render(request, 'sky/engineerSummary.html')  

@login_required(login_url='sky_login')
def departmentleader_summary(request):
    user = request.user

    # Permission check
    if not hasattr(user, 'role') or user.role.strip().lower() != "department leader":
        messages.error(request, "You do not have permission to view this page.")
        return redirect('sky_home')

    # Generate card data (after permission check)
    card_range = range(1, 11)

    # Return the correct page
    return render(request, 'sky/departmentLeaderSummary.html', {'card_range': card_range})


    # Generate 1–10 cards
    card_range = range(1, 11)

@login_required(login_url='sky_login')
def seniormanager_summary(request):
    user = request.user

    if not hasattr(user, 'role') or user.role.strip().lower() != "senior manager":
        messages.error(request, "You do not have permission to view this page.")
        return redirect('sky_home')

    return render(request, 'sky/seniorManagerSummary.html', {
        'card_range': range(1, 11)
    })


#-----------------------------------------------------------------------------------------

# By Shushanik Hayrapetyan

@login_required
def submit_vote(request):
    user = request.user
    session = Session.objects.first()  # use latest or allow selection
    cards = Card.objects.all()

    # Ensure one vote per user/card/session
    for card in cards:
        Vote.objects.get_or_create(user=user, session=session, card=card)

    queryset = Vote.objects.filter(user=user, session=session)
    formset = VoteFormSet(queryset=queryset)

    if request.method == "POST":
        formset = VoteFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            formset.save()
            return redirect('engineer_summary')  

    return render(request, 'sky/vote.html', {'formset': formset})
