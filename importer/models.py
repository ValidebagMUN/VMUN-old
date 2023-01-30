from datetime import datetime
from django.db import models

from institution.models import Institution

# Create your models here.


class Delegation(models.Model):
    email = models.EmailField(help_text='Contact email of the delegation', blank=True, verbose_name='Email')
    active = models.BooleanField(default=True)
    head_delegate = models.OneToOneField('authentication.Delegate', on_delete=models.DO_NOTHING, 
                                         help_text="Head Delegate of the delegation", blank=True, null=True, related_name='head_delegate')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    application_date = models.DateField(help_text='Date of application', default=datetime.now, blank=True, null=True,
                                        verbose_name='Application date')

    class Meta:
        verbose_name = 'delegation'
        verbose_name_plural = 'delegations'

    def __str__(self):
        return self.institution.slug