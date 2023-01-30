from datetime import timedelta
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


# Create your models here.

class GSLSession(models.Model):
    committee = models.ForeignKey("committee.Committee", on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    duration = models.DurationField()
    speakers = models.ManyToManyField("authentication.Delegate", related_name="gsl_speaker")
