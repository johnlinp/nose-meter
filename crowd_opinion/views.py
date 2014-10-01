# -*- coding: utf8 -*-

from django.shortcuts import render
from data_center import models

def home(request):
    return render(request, 'crowd-opinion-home.html')

def district(request, district_name):
    candidates = []

    election_group = models.ElectionGroup.objects.get(id=1)
    election_activity = models.ElectionActivity.objects.get(election_group=election_group, district__name=district_name)
    participations = models.Participation.objects.filter(election_activity=election_activity)

    for participation in participations:
        candidate = {
            'name': participation.candidate.name,
        }
        candidates.append(candidate)

    args = {
        'district_name': district_name,
        'candidates': candidates,
    }

    return render(request, 'crowd-opinion-district.html', args)

def candidate(request, candidate_name):
    candidate = models.Candidate.objects.get(name=candidate_name)
    participations = models.Participation.objects.filter(candidate=candidate, result=models.Participation.ELECTED)

    pa2exp = lambda(participation): \
            str(participation.election_activity.election_group.vote_date.year) + ' ' + \
                    participation.election_activity.district.name + \
                    participation.election_activity.target

    experiences = [pa2exp(participation) for participation in participations]

    promises = models.Promise.objects.filter(participation__candidate=candidate, participation__result=models.Participation.ELECTED)

    fake_promise_scores = [
        '★★☆☆☆',
        '★☆☆☆☆',
        '★★★☆☆',
    ]
    fake_promise_progress = [
        '提案已交付審查',
        '已提出某某提案',
        '某某提案已通過審查',
    ]

    promises_info = []
    for idx, promise in enumerate(promises):
        promise_info = {
            'position': pa2exp(promise.participation),
            'brief': promise.brief,
            'content': promise.content,
            'scores': fake_promise_scores[idx % len(fake_promise_scores)],
            'progress': fake_promise_progress[idx % len(fake_promise_progress)],
        }
        promises_info.append(promise_info)

    educations = [
        '某某大學某某系',
        '某某大學某某所某某組',
    ]

    candidate_info = {
        'name': candidate.name,
        'party': candidate.party,
        'educations': educations,
        'experiences': experiences,
        'promises': promises_info,
    }

    args = {
        'candidate': candidate_info,
    }

    return render(request, 'crowd-opinion-candidate.html', args)

