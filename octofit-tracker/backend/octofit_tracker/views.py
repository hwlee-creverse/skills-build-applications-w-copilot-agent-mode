from rest_framework import viewsets

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout
from .serializers import ActivitySerializer, LeaderboardSerializer, TeamSerializer, UserSerializer, WorkoutSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('name')
    serializer_class = UserSerializer
    lookup_field = 'pk'


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer
    lookup_field = 'pk'


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-recorded_at')
    serializer_class = ActivitySerializer
    lookup_field = 'pk'


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all().order_by('rank')
    serializer_class = LeaderboardSerializer
    lookup_field = 'pk'


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all().order_by('scheduled_for')
    serializer_class = WorkoutSerializer
    lookup_field = 'pk'
