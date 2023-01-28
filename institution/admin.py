from django.contrib import admin
from .models import Institution

# Register your models here.


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'email')
    search_fields = ('name', 'slug', 'email')


admin.site.register(Institution, InstitutionAdmin)
