from rest_framework import serializers

from .models import *

class GSLSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GSLSession
        fields = "__all__"