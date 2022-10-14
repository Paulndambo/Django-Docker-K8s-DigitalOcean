from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FixtureModelViewSet

router = DefaultRouter()
router.register("", FixtureModelViewSet, basename="fixtures")

urlpatterns = [
    path("", include(router.urls)),
]