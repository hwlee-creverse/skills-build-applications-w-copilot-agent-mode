from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=120, unique=True)
    universe = models.CharField(max_length=50)
    motto = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    power_level = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    distance_km = models.FloatField(default=0)
    steps = models.PositiveIntegerField(default=0)
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'


class LeaderboardEntry(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='leaderboard_entry')
    points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'leaderboard'


class Workout(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    workout_name = models.CharField(max_length=120)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField(default=0)
    scheduled_for = models.DateField()

    class Meta:
        db_table = 'workouts'
