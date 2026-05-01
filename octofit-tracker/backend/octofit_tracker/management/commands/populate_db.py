from django.core.management.base import BaseCommand

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Sample data
USERS = [
    {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Steve Rogers", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "DC"},
    {"name": "Clark Kent", "email": "superman@dc.com", "team": "DC"},
]
TEAMS = [
    {"name": "Marvel", "members": ["Tony Stark", "Steve Rogers"]},
    {"name": "DC", "members": ["Bruce Wayne", "Clark Kent"]},
]
ACTIVITIES = [
    {"user": "Tony Stark", "activity": "Running", "duration": 30},
    {"user": "Steve Rogers", "activity": "Cycling", "duration": 45},
    {"user": "Bruce Wayne", "activity": "Swimming", "duration": 25},
    {"user": "Clark Kent", "activity": "Flying", "duration": 60},
]
LEADERBOARD = [
    {"user": "Clark Kent", "points": 100},
    {"user": "Tony Stark", "points": 90},
    {"user": "Steve Rogers", "points": 80},
    {"user": "Bruce Wayne", "points": 70},
]
WORKOUTS = [
    {"name": "Super Strength", "suggested_for": "Clark Kent"},
    {"name": "Genius Tech", "suggested_for": "Tony Stark"},
    {"name": "Shield Training", "suggested_for": "Steve Rogers"},
    {"name": "Stealth", "suggested_for": "Bruce Wayne"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data via ORM
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Insert test data via ORM
        for data in USERS:
            User.objects.create(**data)

        for data in TEAMS:
            Team.objects.create(**data)

        for data in ACTIVITIES:
            Activity.objects.create(**data)

        for data in LEADERBOARD:
            Leaderboard.objects.create(**data)

        for data in WORKOUTS:
            Workout.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
