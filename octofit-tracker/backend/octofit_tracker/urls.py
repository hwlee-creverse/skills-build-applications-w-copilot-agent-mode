import os

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path, reverse
from rest_framework.routers import DefaultRouter

from .views import ActivityViewSet, LeaderboardViewSet, TeamViewSet, UserViewSet, WorkoutViewSet

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workouts')


def api_root(request):
    return JsonResponse(
        {
            'users': f"{base_url}{reverse('users-list')}",
            'teams': f"{base_url}{reverse('teams-list')}",
            'activities': f"{base_url}{reverse('activities-list')}",
            'leaderboard': f"{base_url}{reverse('leaderboard-list')}",
            'workouts': f"{base_url}{reverse('workouts-list')}",
        }
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
