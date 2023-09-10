from django.urls import path
from .           import views




app_name = 'l'


urlpatterns = [
  path('<int:pk>', views.add_cart, name='index'),
  path('Payment', views.payment, name='payment'),
  path('proccess', views.paymentaccepted, name='accept')
]


