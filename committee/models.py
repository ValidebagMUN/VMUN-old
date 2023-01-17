from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Committee(models.Model):
    abv     = models.CharField(max_length=10, help_text="Abbreviation of the committee")
    title   = models.CharField(max_length=100, help_text="Title of the committee")
    desc    = models.TextField(help_text="Description of the committee")
    chair   = models.PositiveSmallIntegerField(help_text="Chair of the committee")
    active  = models.BooleanField(default=True)
    agenda  = models.CharField(max_length=100),
    guide   = models.CharField(max_length=150, help_text="URL to the study guide for the committee")

    def __str__(self):
        return self.abv
    class Meta:
        verbose_name = "committee"
        verbose_name_plural = "committees"

class Session(models.Model):
    committee   = models.ForeignKey(Committee, on_delete=models.CASCADE)
    chair       = models.PositiveSmallIntegerField()
    active      = models.BooleanField(default=True)
    number      = models.PositiveSmallIntegerField(help_text="Number of the session")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "session"
        verbose_name_plural = "sessions"