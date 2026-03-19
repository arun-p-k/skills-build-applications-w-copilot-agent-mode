from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Sample data for users, teams, activities, leaderboard, and workouts
USERS = [
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
]
TEAMS = [
    {"name": "Marvel"},
    {"name": "DC"},
]
ACTIVITIES = [
    {"user": "superman@dc.com", "activity": "Flight", "duration": 60},
    {"user": "batman@dc.com", "activity": "Martial Arts", "duration": 45},
    {"user": "ironman@marvel.com", "activity": "Suit Training", "duration": 50},
]
LEADERBOARD = [
    {"user": "superman@dc.com", "points": 100},
    {"user": "ironman@marvel.com", "points": 90},
]
WORKOUTS = [
    {"name": "Strength Training", "suggested_for": "Marvel"},
    {"name": "Agility Drills", "suggested_for": "DC"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        from django.db import connection
        db = connection.cursor().db_conn.client['octofit_db']
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        db.users.create_index("email", unique=True)
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)
        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
