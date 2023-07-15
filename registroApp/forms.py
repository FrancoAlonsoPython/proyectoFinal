from django import forms
from django.contrib.auth.forms import UserCreationForm
from registroApp.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)