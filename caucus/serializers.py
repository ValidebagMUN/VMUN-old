from rest_framework import serializers
from .models import *

class CaucusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caucus
        fields = '__all__'