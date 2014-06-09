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

    lookup = {
        'district_name': district_name,
        'candidates': candidates,
    }
    return render(request, 'crowd-opinion-district.html', lookup)

def candidate(request, candidate_name):
    candidate = models.Candidate.objects.get(name=candidate_name)
    promises = [
        {
            'position': '某地區市長',
            'content': '認業分著式投加復家費是生往統爸無定類多大接現她們是孩年必政色輕消：新美有不新其了出富間進少者提產不異速府教：政在實精決木機老，似景力回讀多們方家年在臉算種條主，物沒散事中：少或館如我己念風大式送職三驚中華就力如紀火個著會空官不皮意他國市家臺不有人兒英早政想眼使作何級氣回大覺類查兒校怎給友適安調心但又。',
            'scores': '★★☆☆☆',
            'progress': '某某提案已交付審查',
        },
        {
            'position': '某地區立委',
            'content': '怎草一看是帶業學一當盡日人友放要不色大孩工式。不資主但而。靈當信教方明意班美，正作賽好式可的總路黨回現基收所，然識？',
            'scores': '★★★☆☆',
            'progress': '某某提案已通過審查',
        },
        {
            'position': '某地區立委',
            'content': '西出直常指，開美地理毒海我的：預新那大入手力點壓國體畫流子節居價玩高什；出已部復成如料依黃腦多事……地找異，看地資事口腦少費定證。',
            'scores': '★☆☆☆☆',
            'progress': '已提出某某提案',
        },
    ]
    educations = [
        '某某大學某某系',
        '某某大學某某所某某組',
    ]
    experiences = [
        '某地區市長',
        '某地區立委',
    ]
    candidate_info = {
        'name': candidate.name,
        'party': candidate.party,
        'educations': educations,
        'experiences': experiences,
        'promises': promises,
    }
    lookup = {
        'candidate': candidate_info,
    }
    return render(request, 'crowd-opinion-candidate.html', lookup)

