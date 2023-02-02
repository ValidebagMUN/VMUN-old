from rest_framework import serializers
from .models import *

class ChairPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChairPerson
        fields = '__all__'

class DelegateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegate
        fields = '__all__'

class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'