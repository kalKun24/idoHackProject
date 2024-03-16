from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser
from django import forms

class SignupForm(UserCreationForm): 
    class Meta:
        model = CustomUser
        fields = ('username',)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'biography', 'twitter_url', 'github_url', 'linkedin_url', 'country', 'occupation']