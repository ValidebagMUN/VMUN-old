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

resolution_router = routers.NestedSimpleRouter(
    committee_router,
    r'committees',
    lookup='committee'
)
resolution_router.register(r'resolutions', ResolutionViewSet, 'resolutions')

caucus_router = routers.NestedSimpleRouter(
    committee_router,
    r'committees',
    lookup='committee'
)
caucus_router.register(r'caucuses', CaucusViewSet, 'caucuses')

gsl_router = routers.NestedSimpleRouter(
    committee_router,
    r'committees',
    lookup='committee'
)
gsl_router.register(r'gsl', GSLViewSet, 'gsl')

delegation_router = routers.SimpleRouter()
delegation_router.register(r'delegations', DelegationViewSet, 'delegations')

delegate_router = routers.SimpleRouter()
delegate_router.register(r'delegates', DelegateViewSet, 'delegates')

assistant_router = routers.SimpleRouter()
assistant_router.register(r'assistants', AssistantViewSet, 'assistants')

chairperson_router = routers.SimpleRouter()
chairperson_router.register(r'chairpeople', ChairPersonViewSet, 'chairpersons')

institution_router = routers.SimpleRouter()
institution_router.register(r'institutions', InstitutionViewSet, 'institutions')

urlpatterns = [
    path('', include(conference_router.urls)),
    path('', include(committee_router.urls)),
    path('', include(resolution_router.urls)),
    path('', include(caucus_router.urls)),
    path('', include(gsl_router.urls)),
    path('', include(delegation_router.urls)),
    path('', include(delegate_router.urls)),
    path('', include(assistant_router.urls)),
    path('', include(chairperson_router.urls)),
    path('', include(institution_router.urls)),
]