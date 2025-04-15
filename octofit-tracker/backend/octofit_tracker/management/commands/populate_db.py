from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import get_test_data

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        test_data = get_test_data()

        # Populate Users
        # Check if a user with the given username already exists before creating
        for user_data in test_data['users']:
            User.objects.update_or_create(username=user_data['username'], defaults=user_data)

        # Populate Teams
        for team_data in test_data['teams']:
            team_data.pop('description', None)  # Safely remove the field if it exists
            Team.objects.create(**team_data)

        # Populate Activities
        for activity_data in test_data['activities']:
            Activity.objects.create(**activity_data)

        # Populate Leaderboards
        for leaderboard_data in test_data['leaderboards']:
            Leaderboard.objects.create(**leaderboard_data)

        # Populate Workouts
        for workout_data in test_data['workouts']:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
