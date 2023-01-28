from django.db import models
from conference.models import Session, Conference

# Create your models here.


class ChairPerson(models.Model):
    name = models.CharField(max_length=40, help_text='Name of the chairperson')
    email = models.EmailField(help_text='Email of the chairperson')
    phone = models.CharField(max_length=40, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'chairperson'
        verbose_name_plural = 'chairpeople'


class Committee(models.Model):
    slug = models.SlugField(help_text='Abbreviation of the committee', verbose_name='Abbreviation')
    title = models.CharField(max_length=100, help_text='Title of the committee')
    desc = models.TextField(help_text='Description of the committee')
    chair = models.ForeignKey(ChairPerson, on_delete=models.CASCADE, help_text='Chair of the committee')
    agenda = models.TextField(help_text='Agenda items of the committee', null=True, blank=True)
    guide = models.URLField(help_text='URL to the study guide for the committee')
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, help_text='Conference of the committee')
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'committee'
        verbose_name_plural = 'committees'


class CommitteeSession(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, help_text='Committee of the session')
    chair = models.IntegerField(help_text='Id of the chair of the session')
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return self.session.number

    class Meta:
        verbose_name = 'committeesession'
        verbose_name_plural = 'committeesessions'
