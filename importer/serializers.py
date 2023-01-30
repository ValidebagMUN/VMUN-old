from rest_framework import serializers
from .models import *
from authentication.models import *

class DelegationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegation
        fields = '__all__'

class DelegationDelegateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegate
        fields = '__all__'