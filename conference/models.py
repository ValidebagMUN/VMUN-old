from django.db import models
from django.utils import timezone


# Create your models here.

class Conference(models.Model):
    institution = models.CharField(max_length=100, help_text='Institution hosting the conference', blank=True,
                                   verbose_name='Institution')
    name = models.CharField(max_length=100, help_text='Name of the conference', verbose_name='Name')
    slug = models.SlugField(help_text='Slug of the conference', verbose_name='Slug')
    email = models.EmailField(help_text='Contact email of the conference', blank=True, verbose_name='Email')
    website = models.CharField(max_length=100, help_text='Website of the conference', blank=True,
                               verbose_name='Website')
    start_date = models.DateField(help_text='Start date of the conference', default=timezone.now, blank=True, null=True,
                                  verbose_name='Start date')
    end_date = models.DateField(help_text='End date of the conference', blank=True, null=True, verbose_name='End date')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'conference'
        verbose_name_plural = 'conferences'


class Session(models.Model):
    active = models.BooleanField(default=True)
    number = models.PositiveSmallIntegerField(help_text='Number of the session', verbose_name='Number')
    start_time = models.TimeField(help_text='Expected start time of the session', blank=True, null=True,
                                  verbose_name='Start time')
    end_time = models.TimeField(help_text='Expected end time of the session', blank=True, null=True,
                                verbose_name='End time')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'session'
        verbose_name_plural = 'sessions'
