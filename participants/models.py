from django.db import models
from committee.models import Committee
# Create your models here.

class Delegate(models.Model):
    name        = models.CharField(max_length=40, help_text="Name of the delegate")
    email       = models.EmailField(help_text="Email of the delegate")
    phone       = models.CharField(max_length=40, null=True)
    committee   = models.ForeignKey(Committee, on_delete=models.CASCADE)
    country     = models.CharField(max_length=40, help_text="Country of the delegate")
    active      = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "delegate"
        verbose_name_plural = "delegates"

class ChairPerson(models.Model):
    name        = models.CharField(max_length=40, help_text="Name of the chairperson")
    email       = models.EmailField(help_text="Email of the chairperson")
    phone       = models.CharField(max_length=40, null=True)
    active      = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "chairperson"
        verbose_name_plural = "chairpeople"