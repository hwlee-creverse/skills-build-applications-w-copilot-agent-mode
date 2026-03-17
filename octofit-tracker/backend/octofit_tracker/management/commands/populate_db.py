from datetime import date

from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    def handle(self, *args, **options):
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()

        marvel_team = Team.objects.create(
            name='marvel team',
            universe='marvel',
            motto='Avengers, assemble!',
        )
        dc_team = Team.objects.create(
            name='dc team',
            universe='dc',
            motto='Justice for all!',
        )

        users = [
            UserProfile.objects.create(
                name='Iron Man',
                email='ironman@octofit.dev',
                team=marvel_team,
                power_level=95,
            ),
            UserProfile.objects.create(
                name='Captain Marvel',
                email='captainmarvel@octofit.dev',
                team=marvel_team,
                power_level=98,
            ),
            UserProfile.objects.create(
                name='Batman',
                email='batman@octofit.dev',
                team=dc_team,
                power_level=90,
            ),
            UserProfile.objects.create(
                name='Wonder Woman',
                email='wonderwoman@octofit.dev',
                team=dc_team,
                power_level=97,
            ),
        ]

        for index, user in enumerate(users, start=1):
            Activity.objects.create(
                user=user,
                activity_type='Running',
                distance_km=4.0 + index,
                steps=7000 + (index * 1200),
            )
            Workout.objects.create(
                user=user,
                workout_name='HIIT Session',
                duration_minutes=30 + index,
                calories_burned=320 + (index * 35),
                scheduled_for=date(2026, 3, 17),
            )
            LeaderboardEntry.objects.create(
                user=user,
                points=1500 - (index * 100),
                rank=index,
            )

        self.stdout.write(self.style.SUCCESS('테스트 데이터 적재 완료: users, teams, activities, leaderboard, workouts'))
