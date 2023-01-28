from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers

from .views import *

conference_router = routers.SimpleRouter()
conference_router.register(r'conferences', ConferenceViewSet, 'conferences')

committee_router = routers.NestedSimpleRouter(
    conference_router,
    r'conferences',
    lookup='conference'
)
committee_router.register(r'committees', CommitteeViewSet, 'committees')

delegation_router = routers.SimpleRouter()
delegation_router.register(r'delegations', DelegationViewSet, 'delegations')

delegate_router = routers.SimpleRouter()
delegate_router.register(r'delegates', DelegateViewSet, 'delegates')

chairperson_router = routers.SimpleRouter()
chairperson_router.register(r'chairpeople', ChairPersonViewSet, 'chairpersons')

institution_router = routers.SimpleRouter()
institution_router.register(r'institutions', InstitutionViewSet, 'institutions')

urlpatterns = [
    path('', include(conference_router.urls)),
    path('', include(committee_router.urls)),
    path('', include(delegation_router.urls)),
    path('', include(delegate_router.urls)),
    path('', include(chairperson_router.urls)),
    path('', include(institution_router.urls)),
]