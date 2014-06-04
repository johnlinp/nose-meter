from django.shortcuts import render
from data_center import models

def home(request):
    return render(request, 'crowd-opinion-home.html')

def district(request, county_name):
    candidates = []

    election_group = models.ElectionGroup.objects.get(id=1)
    election_activity = models.ElectionActivity.objects.get(election_group=election_group, district__name=county_name)
    participations = models.Participation.objects.filter(election_activity=election_activity)

    for participation in participations:
        candidate = {
            'name': participation.candidate.name,
        }
        candidates.append(candidate)

    lookup = {
        'county_name': county_name,
        'candidates': candidates,
    }
    return render(request, 'crowd-opinion-district.html', lookup)
