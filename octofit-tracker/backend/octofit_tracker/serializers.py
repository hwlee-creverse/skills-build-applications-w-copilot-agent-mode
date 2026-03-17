from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class ObjectIdStringMixin(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)

    def get_id(self, obj):
        return str(obj.pk)


class TeamSerializer(ObjectIdStringMixin):
    class Meta:
        model = Team
        fields = ['id', 'name', 'universe', 'motto']


class UserSerializer(ObjectIdStringMixin):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), allow_null=True, required=False)
    team_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'team', 'team_id', 'power_level']

    def get_team_id(self, obj):
        return str(obj.team_id) if obj.team_id is not None else None


class ActivitySerializer(ObjectIdStringMixin):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    user_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'activity_type', 'distance_km', 'steps', 'recorded_at']

    def get_user_id(self, obj):
        return str(obj.user_id)


class LeaderboardSerializer(ObjectIdStringMixin):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    user_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'user_id', 'points', 'rank']

    def get_user_id(self, obj):
        return str(obj.user_id)


class WorkoutSerializer(ObjectIdStringMixin):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    user_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'user_id', 'workout_name', 'duration_minutes', 'calories_burned', 'scheduled_for']

    def get_user_id(self, obj):
        return str(obj.user_id)
