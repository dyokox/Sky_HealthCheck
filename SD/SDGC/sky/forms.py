from django import forms
from .models import User
# Allows the customization of form fields
from django.forms import TextInput, EmailInput, PasswordInput


# Created a form class for the registration of user
class CreateUserForm(forms.ModelForm):
    class Meta: 
        # Form is based on the User model from models.py
        model = User
        # Fields to include in the form
        fields = ('fullname', 'username', 'email', 'password')
        # Customizing how the fields should be displayed
        widgets = {
            'fullname': TextInput(attrs={'placeholder': 'John Doe'}),
            'username': TextInput(attrs={'placeholder': 'johndoe'}),
            'email': EmailInput(attrs={'placeholder': 'johndoe@gmail.com'}),
            'password': PasswordInput(attrs={'placeholder': 'Password123'}),
        }
    
    # Custom validation for the email, to avoid any duplicates (e.g cannot register with
    # two accounts with the same email)
    def clean_email(self):
        # Gets the email the user entered
        email = self.cleaned_data.get("email")
        # Checks any trace of the email in database
        if User.objects.filter(email=email).exists():
            # Will tell the user if the email is already registered
            raise forms.ValidationError("Email is already registered")
        # If email is not registered already, it can be used
        return email