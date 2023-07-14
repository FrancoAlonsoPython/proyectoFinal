from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm

#class UserRegisterForm(UserCreationForm):
#    email = forms.EmailField()
#    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
# 
#    class Meta:
##       model = CustomUser  
#        fields = ['username', 'email', 'password1', 'password2']
#        help_texts = {k: "" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Email"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"First Name"}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Last Name"}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] #'password'
        help_texts = {k:"" for k in fields}