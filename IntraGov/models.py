from django.db import models
from django.forms import ModelForm


# Create your models here.
PARTIES = (('Democrat', 'Democrat'), ('Republican', 'Republican'), ('Other', 'Other'))

class Politician(models.Model):
    name = models.CharField(max_length=30)
    house = models.CharField(max_length=20)
    state_or_district = models.CharField(max_length=30, blank=True)
    party = models.CharField(max_length=20, choices= PARTIES)
    positions = models.CharField(max_length=20)
    year_elected = models.PositiveIntegerField(blank=True, )

    def __str__(self):
        return self.name


