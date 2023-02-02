from django.db import models
from authentication.models import Delegate
from committee.models import Committee
# Create your models here.


class Caucus(models.Model):
    TYPES = [
        ('MOD', 'Moderated Caucus'),
        ('UNM', 'Un-moderated Caucus'),
        ('SMM', 'Semi-Moderated Caucus'),
    ]
    type = models.CharField(max_length=3, choices=TYPES, default='MOD', verbose_name='Caucus Type')
    topic = models.CharField(max_length=100, verbose_name='Caucus Topic')
    description = models.TextField(verbose_name='Caucus Description', blank=True, null=True)
    start_time = models.DateTimeField(verbose_name='Caucus Start Time')
    duration = models.DurationField(verbose_name='Caucus Duration')
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, verbose_name='Committee', to_field='slug')
    proposer = models.ForeignKey(Delegate, on_delete=models.CASCADE, verbose_name='Proposer of the Caucus')
    participants = models.ManyToManyField(Delegate, verbose_name='Caucus Participants', blank=True,
                                          related_name='caucus_participants')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'caucus'
        verbose_name_plural = 'caucuses'
