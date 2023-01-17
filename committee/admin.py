from django.contrib import admin

# Register your models here.
from .models import Committee, CommitteeSession

admin.site.register(Committee)
admin.site.register(CommitteeSession)