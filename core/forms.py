from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'your name',
        'class'       : 'w-full  py-4 px-6 rounded-xl bg-gray-200  focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all' 
        
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'your password',
        'class'       : 'w-full  py-4 px-6 rounded-xl bg-gray-200 focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all'

    }))
    
# form = LoginForm()    
# form.errors()
# print('*'* 50)
# print(form.error_messages)
# for i in form.error_messages:
#     print(i)
    
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1',  'password2')
        
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'your name',
        'class'       : 'w-full  py-4 px-6 rounded-xl bg-gray-200  focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all' 
        
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'email@',
        'class'       : 'w-full  py-4 px-6 rounded-xl bg-gray-200 focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all'
        
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'your password',
        'class'       : 'w-full  py-4 px-6 rounded-xl bg-gray-200 focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all'
        
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'confirm password',
        'class'       : 'w-full  py-4 px-6 rounded-xl bg-gray-200  focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all'
        
    }))