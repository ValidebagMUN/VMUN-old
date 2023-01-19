from django.conf import settings

def get_settings(request):
   return {'DEBUG': settings.DEBUG, }