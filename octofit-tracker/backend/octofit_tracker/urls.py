from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path, reverse
from rest_framework.routers import DefaultRouter

from .views import ActivityViewSet, LeaderboardViewSet, TeamViewSet, UserViewSet, WorkoutViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workouts')


def api_root(request):
    return JsonResponse(
        {
            'users': request.build_absolute_uri(reverse('users-list')),
            'teams': request.build_absolute_uri(reverse('teams-list')),
            'activities': request.build_absolute_uri(reverse('activities-list')),
            'leaderboard': request.build_absolute_uri(reverse('leaderboard-list')),
            'workouts': request.build_absolute_uri(reverse('workouts-list')),
        }
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/', api_root, name='api-root-legacy'),
    path('api/', include(router.urls)),
]
