from django.shortcuts import render, redirect 
from django.contrib.auth import login 
from .forms import CustomAuthenticationForm, CustomUserRegistrationForm
from django.contrib.auth.views import LoginView
 
def register(request): 
    if request.method == 'POST': 
        form = CustomUserRegistrationForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            login(request, user)  # Вход после регистрации 
            return redirect('vehicles')  # Перенаправление на главную страницу 
    else: 
        form = CustomUserRegistrationForm() 
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
 template_name = 'registration/login.html'
 authentication_form = CustomAuthenticationForm