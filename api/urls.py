from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



urlpatterns = [
    path("getallitems/", views.getallitems, name="getitems"),
    path("getallcars/", views.getallcarstype, name="getitems"),
    path("getalldata/", views.getalldata, name="getalldata"),
    path("checkuser/", views.check_user, name='checkuser'),
    path("createuser/", views.createuser, name="createuser"),
    path("getcart/", views.getcart, name="createuser"),
    path("addtocart/", views.addtocart, name="createuser"),
    path('getitemcartforuser/', views.getitemcartforuser, name='getitemcartforuser'),
    path('getallcartforuser/', views.getallcartforuser, name='getallcartforuser'),
    path('hepaid/', views.hepaid, name='hepaid'),
    path("update_cart/", views.update_cart, name="update_cart"),
    path("deleteoneitemfromcart/", views.deleteoneitemfromcart, name="deleteoneitemfromcart"),
    
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json','xml'])
