from rest_framework.routers import DefaultRouter
from django.urls import path, include

from landing_views.views import LandingViewSet

router = DefaultRouter()
router.register("landing", LandingViewSet, basename="landing")

urlpatterns = [
    path('landing', LandingViewSet.as_view()),
]
