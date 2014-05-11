from django.db import models

class Candidate(models.Model):
    name = models.TextField()
    party = models.TextField()

class District(models.Model):
    name = models.TextField()

class ElectionGroup(models.Model):
    name = models.TextField()
    nickname = models.TextField()
    vote_day = models.DateField()

class ElectionActivity(models.Model):
    election_group = models.ForeignKey(ElectionGroup)
    district = models.ForeignKey(District)
    target = models.TextField()

class Participation(models.Model):
    candidate = models.ForeignKey(Candidate)
    election_activity = models.ForeignKey(ElectionActivity)

class Promise(models.Model):
    participation = models.ForeignKey(Participation)
    brief = models.TextField()
    content = models.TextField()


