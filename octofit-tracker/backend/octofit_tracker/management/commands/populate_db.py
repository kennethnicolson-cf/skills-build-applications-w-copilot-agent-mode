from django.core.management.base import BaseCommand
from django.conf import settings

from django.db import connections

from pymongo import ASCENDING

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
        db = connections['default'].cursor().db_conn
        # Drop collections if they exist
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        # Insert test data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)
        # Ensure unique index on email
        db.users.create_index([("email", ASCENDING)], unique=True)
        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
