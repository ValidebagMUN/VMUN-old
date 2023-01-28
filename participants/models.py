from django.db import models
from django.utils import timezone
from committee.models import Committee
from institution.models import Institution


# Create your models here.

class Delegation(models.Model):
    email = models.EmailField(help_text='Contact email of the delegation', blank=True, verbose_name='Email')
    active = models.BooleanField(default=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    application_date = models.DateField(help_text='Date of application', default=timezone.now, blank=True, null=True,
                                        verbose_name='Application date')

    class Meta:
        verbose_name = 'delegation'
        verbose_name_plural = 'delegations'

    def __str__(self):
        return self.institution.slug


class Delegate(models.Model):
    name = models.CharField(max_length=40, help_text='Name of the delegate')
    email = models.EmailField(help_text='Email of the delegate')
    phone = models.CharField(max_length=40, null=True, help_text='Phone number of the delegate')
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, help_text='Committee of the delegate')
    delegation = models.ForeignKey(Delegation, on_delete=models.DO_NOTHING, help_text='Delegation of the delegate', blank=True, null=True)
    country = models.CharField(max_length=40, help_text='Country of the delegate')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'delegate'
        verbose_name_plural = 'delegates'
