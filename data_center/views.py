# -*- coding: utf8 -*-

from django.shortcuts import render
from data_center import models

def home(request):
    election_groups = models.ElectionGroup.objects.all()
    args = {
        'title': '所有的大選們',
        'buttons': [{'id': election_group.id, 'name': election_group.nickname} for election_group in election_groups],
    }
    return render(request, 'data-center-home.html', args)
