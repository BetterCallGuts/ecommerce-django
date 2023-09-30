from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



urlpatterns = [
    path("getallitems", views.getallitems, name="getitems"),
    path("getallcars", views.getallcarstype, name="getitems"),
    path("getalldata", views.getalldata, name="getalldata"),
    path("checkuser", views.check_user, name='checkuser'),
    path("createuser", views.createuser, name="createuser"),
    
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json','xml'])
