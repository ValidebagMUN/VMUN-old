from django.contrib import admin
from .models import Delegate, Delegation

# Register your models here.


class DelegateAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'committee', 'delegation')
    list_filter = ('delegation', 'committee', 'country')
    search_fields = ('name', 'delegation', 'committee', 'country')


class DelegationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'email', 'application_date')
    list_filter = ('institution', 'application_date')
    search_fields = ('institution', 'email', 'application_date')


admin.site.register(Delegate, DelegateAdmin)
admin.site.register(Delegation, DelegationAdmin)
