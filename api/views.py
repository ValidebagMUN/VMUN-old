from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from VMUN.permissions import *

from .models import *
from .serializers import *

from authentication.models import *
from authentication.serializers import *

from caucus.models import *
from caucus.serializers import *

from committee.models import *
from committee.serializers import *

from conference.models import *
from conference.serializers import *

from gsl.models import *
from gsl.serializers import *

from importer.models import *
from importer.serializers import *

from institution.models import *
from institution.serializers import *

from notifications.models import *
from notifications.serializers import *

from resolution.models import *
from resolution.serializers import *

class AssistantViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AssistantSerializer
    queryset = Assistant.objects.all()

class CaucusViewSet(viewsets.ModelViewSet):
    serializer_class = CaucusSerializer
    queryset = Caucus.objects.all()
    
class ChairPersonViewSet(viewsets.ModelViewSet):
    serializer_class = ChairPersonSerializer
    queryset = ChairPerson.objects.all()

class CommitteeViewSet(viewsets.ModelViewSet):
    serializer_class = CommitteeSerializer
    queryset = Committee.objects.all()
    lookup_field = 'slug'

class CommitteeSessionViewSet(viewsets.ModelViewSet):
    serializer_class = CommitteeSessionSerializer
    queryset = CommitteeSession.objects.all()

class ConferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ConferenceSerializer
    queryset = Conference.objects.all()
    lookup_field = 'slug'

class GSLViewSet(viewsets.ModelViewSet):
    serializer_class = GSLSessionSerializer
    queryset = GSLSession.objects.all()

class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

class InstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()
    lookup_field = 'slug'

class DelegationViewSet(viewsets.ModelViewSet):
    serializer_class = DelegationSerializer
    queryset = Delegation.objects.all()

class DelegateViewSet(viewsets.ModelViewSet):
    serializer_class = DelegateSerializer
    queryset = Delegate.objects.all()

class ResolutionViewSet(viewsets.ModelViewSet):
    serializer_class = ResolutionSerializer
    queryset = Resolution.objects.all()