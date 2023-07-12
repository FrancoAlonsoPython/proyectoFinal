from django.urls import path
from registroApp.views import signup, signup_success

app_name = 'registroApp'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup/success/', signup_success, name='signup_success'),
]