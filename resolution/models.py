from django.db import models
from authentication.models import Delegate
from committee.models import Committee
# Create your models here.


class Resolution(models.Model):
    STATUS = [
        ('D', 'Draft'),
        ('A', 'Amendable'),
        ('P', 'Passed'),
        ('F', 'Failed'),
    ]
    sponsors = models.ManyToManyField(Delegate, related_name='sponsors')
    signatories = models.ManyToManyField(Delegate, related_name='signatories', blank=True)
    topic = models.CharField(max_length=100)
    file = models.URLField()
    status = models.CharField(max_length=1, choices=STATUS, default='D')
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'resolution'
        verbose_name_plural = 'resolutions'
