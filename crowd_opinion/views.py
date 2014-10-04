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
    participations = models.Participation.objects. \
            filter(candidate=candidate, result=models.Participation.ELECTED). \
            order_by('-election_activity__election_group__vote_date')

    fake_promise_evaluations = [
        ('★★☆☆☆', '提案已交付審查', [
            {
                'target': '某甲提案',
                'state': '已交付審查',
                'link': 'javascript: void(0);'
            },
            {
                'target': '某乙提案',
                'state': '已交付審查',
                'link': 'javascript: void(0);'
            },
        ]),
        ('★☆☆☆☆', '已提出提案', [
            {
                'target': '某丙提案',
                'state': '已提出',
                'link': 'javascript: void(0);'
            },
        ]),
        ('★★★☆☆', '提案已通過審查', [
            {
                'target': '某丁提案',
                'state': '已通過審查',
                'link': 'javascript: void(0);'
            },
            {
                'target': '某戊提案',
                'state': '已通過審查',
                'link': 'javascript: void(0);'
            },
            {
                'target': '某己提案',
                'state': '已通過審查',
                'link': 'javascript: void(0);'
            },
        ]),
    ]

    experiences = []
    for participation in participations:
        promises = models.Promise.objects.filter(participation=participation)
        promises_info = []
        for idx, promise in enumerate(promises):
            evaluation = fake_promise_evaluations[idx % len(fake_promise_evaluations)]
            promise_info = {
                'brief': promise.brief,
                'content': promise.content,
                'scores': evaluation[0],
                'status': evaluation[1],
                'progresses': evaluation[2],
            }
            promises_info.append(promise_info)

        experience_name = str(participation.election_activity.election_group.vote_date.year) + ' ' + \
                participation.election_activity.district.name + \
                participation.election_activity.target

        experience = {
            'name': experience_name,
            'promises': promises_info,
        }
        experiences.append(experience)

    educations = [
        '某某大學某某系',
        '某某大學某某所某某組',
    ]

    candidate_info = {
        'name': candidate.name,
        'party': candidate.party,
        'educations': educations,
        'experiences': experiences,
    }

    args = {
        'candidate': candidate_info,
    }

    return render(request, 'crowd-opinion-candidate.html', args)

def about_stars(request):
    return render(request, 'crowd-opinion-about-stars.html')

