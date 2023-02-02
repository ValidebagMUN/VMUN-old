from django.contrib import admin

# Register your models here.
from .models import Committee, CommitteeSession


class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'chairperson', 'assistant', 'agenda', 'guide')
    list_filter = ('slug', 'chairperson')
    search_fields = ('slug', 'title', 'chairperson')

admin.site.register(Committee, CommitteeAdmin)


class CommitteeSessionAdmin(admin.ModelAdmin):
    list_display = ('committee', 'session')
    list_filter = ('committee', 'session')
    search_fields = ('committee', 'session')


admin.site.register(CommitteeSession, CommitteeSessionAdmin)