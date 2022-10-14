from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import FixtureSerializer
from .models import Fixture
# Create your views here.
class FixtureModelViewSet(ModelViewSet):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer