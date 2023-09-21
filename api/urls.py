from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



urlpatterns = [
    path("getallitems", views.getallitems, name="getitems"),
    path("getallcars", views.getallcarstype, name="getitems")
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json','xml'])
