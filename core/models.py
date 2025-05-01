from django.db import models

# Create your models here.
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
from django.db import models

class HealthCard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Session(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
