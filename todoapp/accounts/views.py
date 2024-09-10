from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views import View

# Create your views here.

class  LoginView(BaseLoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy('home')


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')