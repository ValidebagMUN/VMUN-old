from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers

from .views import *

api_router = routers.DefaultRouter()
api_router.register(r'conferences', ConferenceViewSet, 'conferences')
api_router.register(r'delegations', DelegationViewSet, 'delegations')
api_router.register(r'delegates', DelegateViewSet, 'delegates')
api_router.register(r'assistants', AssistantViewSet, 'assistants')
api_router.register(r'chairpeople', ChairPersonViewSet, 'chairpersons')
api_router.register(r'institutions', InstitutionViewSet, 'institutions')

delegation_subrouter = routers.NestedDefaultRouter(
    api_router,
    r'delegations',
    lookup='delegation'
)
delegation_subrouter.register(r'delegates', DelegationDelegateViewSet, 'delegates')

conference_subrouter = routers.NestedDefaultRouter(
    api_router,
    r'conferences',
    lookup='conference'
)
conference_subrouter.register(r'committees', CommitteeViewSet, 'committees')

committee_subrouter = routers.NestedDefaultRouter(
    conference_subrouter,
    r'committees',
    lookup='committee'
)
committee_subrouter.register(r'resolutions', ResolutionViewSet, 'resolutions')
committee_subrouter.register(r'caucuses', CaucusViewSet, 'caucuses')
committee_subrouter.register(r'gsl', GSLViewSet, 'gsl')


urlpatterns = [
    path('', include(api_router.urls)),
    path('', include(conference_subrouter.urls)),
    path('', include(committee_subrouter.urls)),
    path('', include(delegation_subrouter.urls)),
]
