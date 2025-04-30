from django.db import models
from django.contrib.auth.models import AbstractUser

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

