from django.contrib import admin
# Imports custom model from models.py
from .models import User

# Makes the model manageable from the Django Admin Panel
admin.site.register(User)