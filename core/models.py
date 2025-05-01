from django.db import models

# --- Teams ---
class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# --- Health Cards ---
class HealthCard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# --- Sessions ---
class Session(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} on {self.date.strftime('%Y-%m-%d')}"
