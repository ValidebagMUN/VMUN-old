from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *

from caucus.models import *
from caucus.serializers import *

from committee.models import *
from committee.serializers import *

from conference.models import *
from conference.serializers import *

from institution.models import *
from institution.serializers import *

from participants.models import *
from participants.serializers import *

from resolution.models import *
from resolution.serializers import *


# Create your views here.


class CaucusViewSet(viewsets.ModelViewSet):
    serializer_class = CaucusSerializer
    queryset = Caucus.objects.all()
    
class ChairPersonViewSet(viewsets.ModelViewSet):
    serializer_class = ChairPersonSerializer
    queryset = ChairPerson.objects.all()

class CommitteeViewSet(viewsets.ModelViewSet):
    serializer_class = CommitteeSerializer
    queryset = Committee.objects.all()

class CommitteeSessionViewSet(viewsets.ModelViewSet):
    serializer_class = CommitteeSessionSerializer
    queryset = CommitteeSession.objects.all()

class ConferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ConferenceSerializer
    queryset = Conference.objects.all()

class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

class InstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()

class DelegationViewSet(viewsets.ModelViewSet):
    serializer_class = DelegationSerializer
    queryset = Delegation.objects.all()

class DelegateViewSet(viewsets.ModelViewSet):
    serializer_class = DelegateSerializer
    queryset = Delegate.objects.all()

class ResolutionViewSet(viewsets.ModelViewSet):
    serializer_class = ResolutionSerializer
    queryset = Resolution.objects.all()