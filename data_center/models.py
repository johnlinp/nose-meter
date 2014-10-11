from django.db import models

class Candidate(models.Model):
    name = models.TextField()
    party = models.TextField()

class District(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name.encode('utf8')

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
    TBD = 'tbd'
    ELECTED = 'elected'
    FAILED = 'failed'
    RESULT_CHOICES = (
        (TBD, 'tbd'),
        (ELECTED, 'elected'),
        (FAILED, 'failed'),
    )
    candidate = models.ForeignKey(Candidate)
    election_activity = models.ForeignKey(ElectionActivity)
    result = models.CharField(max_length=255, choices=RESULT_CHOICES, default=TBD)

    def __str__(self):
        return self.candidate.name.encode('utf8')

class Promise(models.Model):
    participation = models.ForeignKey(Participation)
    brief = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.brief.encode('utf8')

class Reference(models.Model):
    participation = models.ForeignKey(Participation)
    url = models.TextField()

class Tag(models.Model):
    name = models.TextField()

class HasTag(models.Model):
    promise = models.ForeignKey(Promise)
    tag = models.ForeignKey(Tag)

