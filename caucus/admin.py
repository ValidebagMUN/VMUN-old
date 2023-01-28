from django.contrib import admin
from .models import Caucus


# Register your models here.


class CaucusAdmin(admin.ModelAdmin):
    list_display = ('type', 'start_time', 'duration', 'committee', 'proposer')
    list_filter = ('type', 'duration', 'committee')
    search_fields = ('topic', 'description', 'committee__name', 'proposer__name')


admin.site.register(Caucus, CaucusAdmin)
