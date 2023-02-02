from django.contrib import admin
from .models import Delegation

# Register your models here.

class DelegationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'email', 'application_date')
    list_filter = ('institution', 'application_date')
    search_fields = ('institution', 'email', 'application_date')

admin.site.register(Delegation, DelegationAdmin)
