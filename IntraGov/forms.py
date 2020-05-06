from django.forms import ModelForm
from .models import Politician

class PoliticianForm(ModelForm):
    class Meta:
        model = Politician
        fields = ['name',
                  'house',
                  'state_or_district',
                  'party',
                  'positions',
                  'year_elected']
