from django.urls import path
from django.contrib.auth.views import LogoutView
from registroApp.views import login_request, signup

app_name = 'registroApp'

urlpatterns = [
    path('login/', login_request, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(template_name="registroApp/login/login.html"), name="Logout"),
    ]
