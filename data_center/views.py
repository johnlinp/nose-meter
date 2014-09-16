# -*- coding: utf8 -*-

from django.shortcuts import render
from django.shortcuts import redirect
from data_center import models


def show_all(request, eg_id=None, ea_id=None, p_id=None):
    election_group = None

    if eg_id is None:
        subject = 'election-group'
    elif ea_id is None:
        subject = 'election-activity'
    elif p_id is None:
        subject = 'candidate'
    else:
        raise

    title = _get_show_title(subject, eg_id, ea_id, p_id)
    buttons = _get_show_buttons(subject, eg_id, ea_id, p_id)
    inputs = _get_show_inputs(subject, request.path, eg_id, ea_id, p_id)

    args = {
        'title': title,
        'buttons': buttons,
        'inputs': inputs,
    }

    return render(request, 'data-center-show.html', args)


def insert_all(request):
    if request.method != 'POST':
        return redirect('/data/')

    redirect_path = request.POST['redirect']
    subject = request.POST['subject']

    if subject == 'election-group':
        election_group_name = request.POST['name']
        election_group_nickname = request.POST['nickname']
        election_group_vote_date = request.POST['vote-date']
    elif subject == 'election-activity':
        election_group_id = request.POST['election-group-id']
        district_name = request.POST['district-name']
        election_activity_target = request.POST['target']
    elif subject == 'candidate':
        election_activity_id = request.POST['election-activity-id']
        candidate_name = request.POST['name'].strip()
        candidate_party = request.POST['party'].strip()
        participation_result = request.POST['result'].strip()

        if candidate_name == '' or candidate_party == '' or participation_result == '':
            return render(request, 'data-center-error.html', {'message': '候選人資料不可以是空白!'})
        elif participation_result != 'tbd' and participation_result != 'elected':
            return render(request, 'data-center-error.html', {'message': '投票結果只能是 tbd 或是 elected!'})

        election_activity = models.ElectionActivity.objects.get(id=election_activity_id)

        try:
            candidate = models.Candidate.objects.get(name=candidate_name)
        except models.Candidate.DoesNotExist:
            candidate = models.Candidate(name=candidate_name, party=candidate_party)
            candidate.save()

        try:
            participation = models.Participation.objects.get(candidate=candidate, election_activity=election_activity)
            return render(request, 'data-center-error.html', {'message': '這個候選人已經在這次選舉裡啦!'})
        except models.Participation.DoesNotExist:
            participation = models.Participation(candidate=candidate,
                    election_activity=election_activity,
                    result=participation_result)
            participation.save()
    else:
        raise

    return redirect(redirect_path)


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


def _get_show_title(subject, eg_id, ea_id, p_id):
    if subject == 'election-group':
        title = '所有的大選們'
    elif subject == 'election-activity':
        election_group = models.ElectionGroup.objects.get(id=eg_id)
        title = str(election_group)
    elif subject == 'candidate':
        election_activity = models.ElectionActivity.objects.get(id=ea_id)
        title = str(election_activity)
    else:
        raise

    return title

def _get_show_buttons(subject, eg_id, ea_id, p_id):
    if subject == 'election-group':
        election_groups = models.ElectionGroup.objects.all()
        items = election_groups
        levels = []
    elif subject == 'election-activity':
        election_group = models.ElectionGroup.objects.get(id=eg_id)
        election_activities = models.ElectionActivity.objects.filter(election_group=election_group)
        items = election_activities
        levels = [eg_id]
    elif subject == 'candidate':
        election_group = models.ElectionGroup.objects.get(id=eg_id)
        election_activity = models.ElectionActivity.objects.get(id=ea_id)
        participations = models.Participation.objects.filter(election_activity=election_activity)
        items = participations
        levels = [eg_id, ea_id]
    else:
        raise

    buttons = []
    for item in items:
        button = {
            'levels': '/'.join([str(num) for num in (levels + [item.id])]),
            'name': str(item),
        }
        buttons.append(button)

    return buttons

def _get_show_inputs(subject, path, eg_id, ea_id, p_id):
    if subject == 'election-group':
        items = [
            {
                'explicit': True,
                'name': 'name',
                'title': '大選全名',
                'placeholder': '比較正式的名稱',
            },
            {
                'explicit': True,
                'name': 'nickname',
                'title': '大選暱稱',
                'placeholder': '口頭上會講的',
            },
            {
                'explicit': True,
                'name': 'vote-date',
                'title': '投票日期',
                'placeholder': '格式請輸入 2014/2/23',
            },
        ]
    elif subject == 'election-activity':
        items = [
            {
                'explicit': False,
                'name': 'election-group-id',
                'value': eg_id,
            },
            {
                'explicit': True,
                'name': 'district-name',
                'title': '選區',
                'placeholder': '請填全稱',
            },
            {
                'explicit': True,
                'name': 'target',
                'title': '職位',
                'placeholder': '像是 "市長" 、 "縣長" 、 "立法委員" 等等',
            },
        ]
    elif subject == 'candidate':
        items = [
            {
                'explicit': False,
                'name': 'election-activity-id',
                'value': ea_id,
            },
            {
                'explicit': True,
                'name': 'name',
                'title': '候選人名稱',
                'placeholder': '請填全名',
            },
            {
                'explicit': True,
                'name': 'party',
                'title': '候選人政黨',
                'placeholder': '請填全名',
            },
            {
                'explicit': True,
                'name': 'result',
                'title': '選舉結果',
                'placeholder': '請填 tbd 或是 elected',
            },
        ]
    else:
        raise

    inputs = {
        'subject': subject,
        'redirect': path,
        'list': items,
    }

    return inputs

