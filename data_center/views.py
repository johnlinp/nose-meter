# -*- coding: utf8 -*-

from django.shortcuts import render
from data_center import models

def show_all(request, eg_id=None, ea_id=None):
    election_group = None

    levels = []
    if eg_id is None:
        election_groups = models.ElectionGroup.objects.all()
        items = election_groups
        title = '所有的大選們'
    else:
        election_group = models.ElectionGroup.objects.get(id=eg_id)
        election_activities = models.ElectionActivity.objects.filter(election_group=election_group)
        items = election_activities
        title = election_group.nickname
        levels.append(str(eg_id))

    buttons = []
    for item in items:
        button = {
            'levels': '/'.join(levels + [str(item.id)]),
            'name': str(item),
        }
        buttons.append(button)

    args = {
        'title': title,
        'buttons': buttons,
    }
       
    return render(request, 'data-center-show.html', args)

