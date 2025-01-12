from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser 

class CustomUserCreationForm(UserCreationForm): 
    class Meta: 
        model = CustomUser 
        fields = ['username', 'password1', 'password2'] 

class CustomUserRegistrationForm(UserCreationForm):
   username = forms.CharField(
      label="Логин",
      widget=forms.TextInput(attrs={
         'class':'form-control',
         'placeholder': 'Введите логин',
      })
   )        
   password1 = forms.CharField(
      label = 'Пароль',
      widget=forms.PasswordInput(attrs={
         'class':'form-control',
         'placeholder': 'Введите пароль',
      })
   )
   password2 = forms.CharField(
      label = 'Повторите пароль',
      widget=forms.PasswordInput(attrs={
         'class':'form-control',
         'placeholder': 'Повторите пароль',
      })
   )
   class Meta:
      model = CustomUser
      fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Логин',
 }))
    password = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={
    'class': 'form-control',
    'placeholder': 'Пароль',
 }))
    