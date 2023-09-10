from django.urls import path
from . import views


app_name = 'conv'
urlpatterns = [
    path('<int:pk>/', views.detailconv  , name="detailconv"),
    path('', views.inbox , name='inbox'),
    path('new/<int:item_pk>/', views.new_conv , name='new')
]
