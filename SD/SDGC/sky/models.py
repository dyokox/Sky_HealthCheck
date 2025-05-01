# Authored by Corina Muntean, Callum Walters, Shushanik Hayrapetyan


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


#------------------------------------------------------------------------------------------
# By Corina Muntean // w1993775

# Creating a custom user model, which inherits from Django's AbstractUser
class User(AbstractUser):
    fullname = models.CharField(max_length=255)
    # Stores the role of the user, default is Engineer
    # A higher power than Engineer has to change their role
    role = models.CharField(max_length=50, default="Engineer")

    # Specifying which field will be used to log in
    # Its using username isntead of email or fullname etc
    USERNAME_FIELD = 'username'
    # Fields that are required to create a user
    REQUIRED_FIELDS = ['email', 'fullname']

    # Representation of the user object when printed or displayed
    # This is also how it will be shown in the Django Admin Panel
    def __str__(self):
        return f"{self.fullname} - {self.username}"
#-----------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
# By Callum Walters

# New model to store votes
class Vote(models.Model):
    VOTE_CHOICES = [
        ('green', 'Green'),
        ('amber', 'Amber'),
        ('red', 'Red'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.CharField(max_length=50)
    session = models.CharField(max_length=50)
    choice = models.CharField(max_length=10, choices=VOTE_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} voted {self.choice} on {self.card} in {self.session}"
#--------------------------------------------------------------------------------------------------

# By Shushanik Hayrapetyan-w1969574

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    ROLE_CHOICES = [
        ('engineer', 'Engineer'),
        ('team_lead', 'Team Lead'),
        ('department_lead', 'Department Lead'),
        ('senior_manager', 'Senior Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Session(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Vote(models.Model):
    VOTE_CHOICES = [
        ('red', 'Red'),
        ('amber', 'Amber'),
        ('green', 'Green'),
    ]
    PROGRESS_CHOICES = [
        ('better', 'Getting Better'),
        ('worse', 'Getting Worse'),
        ('same', 'No Change'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    vote = models.CharField(max_length=10, choices=VOTE_CHOICES)
    progress = models.CharField(max_length=10, choices=PROGRESS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'session', 'card')

    def __str__(self):
        return f"{self.user.username} - {self.card.title} ({self.vote})"
