from django.db import models


# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the institution', verbose_name='Name')
    slug = models.SlugField(help_text='Slug of the institution', verbose_name='Slug')
    email = models.EmailField(help_text='Contact email of the institution', blank=True, verbose_name='Email')
    website = models.CharField(max_length=100, help_text='Website of the institution', blank=True,
                               verbose_name='Website')
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'institution'
        verbose_name_plural = 'institutions'

    def __str__(self):
        return self.slug
