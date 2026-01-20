from django.test import TestCase
from .models import UserProfile, Team, Activity, LeaderboardEntry, Workout

class UserProfileModelTest(TestCase):
    def test_create_user_profile(self):
        user = UserProfile.objects.create(user_id='u1', display_name='Test User', email='test@example.com')
        self.assertEqual(user.display_name, 'Test User')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Team A', description='A test team')
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_id='u1', activity_type='run', duration=30)
        self.assertEqual(activity.activity_type, 'run')

class LeaderboardEntryModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        entry = LeaderboardEntry.objects.create(user_id='u1', score=100, rank=1, week='2024-01-01')
        self.assertEqual(entry.rank, 1)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(workout.name, 'Pushups')
