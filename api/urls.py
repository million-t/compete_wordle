from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WordViewSet, ContestViewSet, GuessViewSet, ContestParticipantViewSet

router = DefaultRouter()
router.register(r'words', WordViewSet)
router.register(r'contests', ContestViewSet)
router.register(r'guesses', GuessViewSet)
router.register(r'contest-participants', ContestParticipantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]