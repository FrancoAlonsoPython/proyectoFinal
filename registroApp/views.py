from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registroApp:signup_success')
    else:
        form = UserRegisterForm()
    
    return render(request,  'registroApp/signup.html', {'form': form})

def signup_success(request):
    return render(request, 'signup_success.html')

