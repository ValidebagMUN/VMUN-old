from django.contrib import admin
from .models import Delegate, Delegation, ChairPerson

# Register your models here.
admin.site.register(Delegate)
admin.site.register(Delegation)
admin.site.register(ChairPerson)
