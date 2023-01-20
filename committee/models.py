from django.db import models
from conference.models import Session


# Create your models here.
class Committee(models.Model):
    slug = models.SlugField(help_text='Abbreviation of the committee', verbose_name='Abbreviation')
    title = models.CharField(max_length=100, help_text='Title of the committee')
    desc = models.TextField(help_text='Description of the committee')
    chair = models.IntegerField(help_text='Id of the chair of the committee')
    active = models.BooleanField(default=True)
    agenda = models.CharField(max_length=100),
    guide = models.CharField(max_length=150, help_text='URL to the study guide for the committee')

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
