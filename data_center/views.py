# -*- coding: utf8 -*-

from django.shortcuts import render
from data_center import models


def show_all(request, eg_id=None, ea_id=None, p_id=None):
    election_group = None

    if eg_id is None:
        election_groups = models.ElectionGroup.objects.all()
        items = election_groups
        title = '所有的大選們'
        levels = []
    elif ea_id is None:
        election_group = models.ElectionGroup.objects.get(id=eg_id)
        election_activities = models.ElectionActivity.objects.filter(election_group=election_group)
        items = election_activities
        title = str(election_group)
        levels = [eg_id]
    else:
        election_group = models.ElectionGroup.objects.get(id=eg_id)
        election_activity = models.ElectionActivity.objects.get(id=ea_id)
        participations = models.Participation.objects.filter(election_activity=election_activity)
        items = participations
        title = str(election_activity)
        levels = [eg_id, ea_id]

    buttons = []
    for item in items:
        button = {
            'levels': '/'.join([str(num) for num in (levels + [item.id])]),
            'name': str(item),
        }
        buttons.append(button)

    args = {
        'title': title,
        'buttons': buttons,
    }
       
    return render(request, 'data-center-show.html', args)

def show_tmp(request):
    election_group = models.ElectionGroup.objects.get(id=1)
    election_activities = models.ElectionActivity.objects.filter(election_group=election_group)
    items = []
    for election_activity in election_activities:
        participations = models.Participation.objects.filter(election_activity=election_activity)
        for participation in participations:
            candidate = participation.candidate
            item = {
                'content': election_activity.district.name + ',' + candidate.name + ',' + candidate.party,
            }
            items.append(item)

    args = {
        'title': '九合一候選人們',
        'items': items,
    }
       
    return render(request, 'data-center-tmp.html', args)

