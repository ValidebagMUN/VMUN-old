from django.contrib import admin
from .models import *

# Register your models here.

class DelegateAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'committee', 'institution','country']
    search_fields = ['name', 'email', 'phone', 'institution','country']
    ordering = ('name',)
    filter_horizontal = ()

admin.site.register(Delegate, DelegateAdmin)

class ChairPersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'committee']

admin.site.register(ChairPerson, ChairPersonAdmin)

class AssistantAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'committee']


admin.site.register(Assistant, AssistantAdmin)