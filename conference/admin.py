from django.contrib import admin
from .models import Conference, Session

# Register your models here.


class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'start_date', 'end_date', 'active')
    list_filter = ('active',)
    search_fields = ('name', 'institution', 'start_date', 'end_date')


class SessionAdmin(admin.ModelAdmin):
    list_display = ('number', 'start_time', 'end_time', 'active')
    list_filter = ('active',)
    search_fields = ('number', 'start_time', 'end_time')


admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Session, SessionAdmin)
