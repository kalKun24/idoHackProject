from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate

from .forms import SignupForm
from .models import CustomUser

def LogoutView(request):
    logout(request)
    return redirect('index')

class SignupView(CreateView):
    model = CustomUser
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response
    

class ProfileView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'account/profile.html'
    context_object_name = 'profile_list'

    def get_queryset(self):
        if CustomUser.objects.filter(username=self.kwargs['playername']).exists():
            return CustomUser.objects.filter(username=self.kwargs['playername'])    
        else:
            return CustomUser.objects.filter(username=self.request.user.username)
    
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['username', 'email', 'biography', 'twitter_url', 'github_url', 'linkedin_url', 'country', 'occupation']
    template_name = 'account/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return CustomUser.objects.get(username=self.request.user.username)