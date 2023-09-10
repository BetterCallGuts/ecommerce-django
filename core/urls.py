from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from . import views

app_name = 'core'

urlpatterns = [
    path('store/', views.index , name='index'),
    path('', views.landing, name='landing'),
    path("contact/" , views.contact, name='contact'),
    path("signup/" , views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_user ,name='logout')

]

