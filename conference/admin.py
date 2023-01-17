from django.contrib import admin

# Register your models here.
from .models import Conference, Session

admin.site.register(Conference)
admin.site.register(Session)