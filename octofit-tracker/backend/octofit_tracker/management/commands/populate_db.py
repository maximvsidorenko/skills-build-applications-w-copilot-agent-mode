from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import get_test_data
from datetime import timedelta

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
        # Convert 'calories_burned' to a timedelta object for the 'duration' field
        for activity_data in test_data['activities']:
            Activity.objects.update_or_create(activity_type=activity_data['name'], defaults={
                'duration': timedelta(minutes=activity_data['calories_burned'])  # Assuming calories burned maps to minutes
            })

        # Populate Leaderboard
        for leaderboard_data in test_data['leaderboard']:
            user = User.objects.get(username=leaderboard_data['user'])
            Leaderboard.objects.create(user=user, score=leaderboard_data['score'])

        # Populate Workouts
        # Update Workout population to use 'name' and 'description' fields
        for workout_data in test_data['workouts']:
            Workout.objects.create(name=workout_data['name'], description=workout_data['activity'])

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
