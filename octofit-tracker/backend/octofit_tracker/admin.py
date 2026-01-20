from django.contrib import admin
from .models import UserProfile, Team, Activity, LeaderboardEntry, Workout

admin.site.register(UserProfile)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(LeaderboardEntry)
admin.site.register(Workout)
