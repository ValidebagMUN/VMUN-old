from rest_framework import serializers
from .models import *

class ResolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resolution
        fields = '__all__'