from rest_framework import serializers
from .models import *

class ChairPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChairPerson
        fields = '__all__'

class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committee
        fields = '__all__'

class CommitteeSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeSession
        fields = '__all__'