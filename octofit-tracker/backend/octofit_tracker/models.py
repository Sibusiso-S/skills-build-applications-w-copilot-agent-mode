from django.db import models

# User model (for reference, actual user management via django-allauth)
class UserProfile(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=255, blank=True, null=True)
    # Add additional profile fields as needed

# Team model
class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    members = models.JSONField(default=list)  # List of user_ids

# Activity model
class Activity(models.Model):
    user_id = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=100)
    duration = models.FloatField()  # in minutes
    distance = models.FloatField(blank=True, null=True)  # in km
    timestamp = models.DateTimeField(auto_now_add=True)

# Leaderboard model
class LeaderboardEntry(models.Model):
    user_id = models.CharField(max_length=255)
    score = models.FloatField()
    rank = models.IntegerField()
    week = models.DateField()

# Workout model
class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    suggested_for = models.JSONField(default=list)  # List of user_ids or team names
