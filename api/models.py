from django.db import models

# Create your models here.
RESULT_CHOICES = (
    ("home_win", "Home Win"),
    ("away_win", "Away Win"),
    ("draw", "Draw"),
)

class Fixture(models.Model):
    home_team = models.CharField(max_length=200)
    home_squad = models.JSONField(null=True)
    away_team = models.CharField(max_length=200)
    away_squad = models.JSONField(null=True)
    stadium = models.CharField(max_length=200, null=True, blank=True)
    results = models.CharField(max_length=200, null=True, blank=True, choices=RESULT_CHOICES)
    score = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.home_team + "Vs. " + self.away_team