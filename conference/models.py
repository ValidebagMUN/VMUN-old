from django.db import models

# Create your models here.

class Conference:
    institution = models.CharField(max_length=100, help_text="Institution hosting the conference")
    name        = models.CharField(max_length=100, help_text="Name of the conference")
    email       = models.EmailField(help_text="Contact email of the conference")