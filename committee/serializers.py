from rest_framework import serializers
from .models import *


class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committee
        fields = '__all__'

class CommitteeSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeSession
        fields = '__all__'