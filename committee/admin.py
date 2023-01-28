from django.contrib import admin

# Register your models here.
from .models import Committee, CommitteeSession, ChairPerson


class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'chair', 'agenda', 'guide')
    list_filter = ('slug', 'chair')
    search_fields = ('slug', 'title', 'chair')


class CommitteeSessionAdmin(admin.ModelAdmin):
    list_display = ('committee', 'chair', 'session')
    list_filter = ('committee', 'chair')
    search_fields = ('committee', 'chair', 'session')


class ChairPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'committee', 'email')
    list_filter = ('name', 'committee')
    search_fields = ('name',)


admin.site.register(Committee, CommitteeAdmin)
admin.site.register(CommitteeSession)
admin.site.register(ChairPerson, ChairPersonAdmin)
