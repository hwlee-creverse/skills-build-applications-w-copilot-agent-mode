from datetime import date

from django.test import TestCase
from rest_framework.test import APIClient

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class OctofitApiCollectionsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='marvel team', universe='marvel', motto='assemble')
        self.user = UserProfile.objects.create(
            name='Iron Man',
            email='ironman@test.dev',
            team=self.team,
            power_level=95,
        )
        Activity.objects.create(user=self.user, activity_type='Running', distance_km=5.5, steps=8000)
        LeaderboardEntry.objects.create(user=self.user, points=1400, rank=1)
        Workout.objects.create(
            user=self.user,
            workout_name='HIIT Session',
            duration_minutes=30,
            calories_burned=350,
            scheduled_for=date(2026, 3, 17),
        )

    def test_all_collection_endpoints_are_available(self):
        endpoints = [
            '/api/users/',
            '/api/teams/',
            '/api/activities/',
            '/api/leaderboard/',
            '/api/workouts/',
        ]

        for endpoint in endpoints:
            response = self.client.get(endpoint)
            self.assertEqual(response.status_code, 200)
            self.assertGreaterEqual(len(response.json()), 1)
