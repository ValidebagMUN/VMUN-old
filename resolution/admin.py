from django.contrib import admin
from .models import Resolution


# Register your models here.


class ResolutionAdmin(admin.ModelAdmin):
    list_display = ('topic', 'status', 'committee')
    list_filter = ('committee', 'status')
    search_fields = ('topic', 'sponsors', 'signatories')


admin.site.register(Resolution, ResolutionAdmin)
