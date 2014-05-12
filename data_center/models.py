from django.db import models

class Candidate(models.Model):
    name = models.TextField()
    party = models.TextField()

class District(models.Model):
    name = models.TextField()

class ElectionGroup(models.Model):
    name = models.TextField()
    nickname = models.TextField()
    vote_date = models.DateField()

    def __str__(self):
        return self.nickname.encode('utf8')

class ElectionActivity(models.Model):
    election_group = models.ForeignKey(ElectionGroup)
    district = models.ForeignKey(District)
    target = models.TextField()

    def __str__(self):
        return self.district.name.encode('utf8') + ' - ' + self.target.encode('utf8')

class Participation(models.Model):
    candidate = models.ForeignKey(Candidate)
    election_activity = models.ForeignKey(ElectionActivity)

    def __str__(self):
        return self.candidate.name.encode('utf8')

class Promise(models.Model):
    participation = models.ForeignKey(Participation)
    brief = models.TextField()
    content = models.TextField()

