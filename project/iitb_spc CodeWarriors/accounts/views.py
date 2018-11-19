from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# class Login(generic.CreateView):
#     #next = 'home'
#     template_name = 'login.html'
#     success_url = reverse_lazy('home')
    
# Create your views here.
