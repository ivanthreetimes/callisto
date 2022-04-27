from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from callisto.auth_app.forms import AppUserRegistrationForm


class AppUserRegistrationView(views.CreateView):
    form_class = AppUserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('user login')


class AppUserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'
    # success_url = reverse_lazy('index')


class AppUserLogoutView(auth_views.LogoutView):
    template_name = 'auth/logout.html'
