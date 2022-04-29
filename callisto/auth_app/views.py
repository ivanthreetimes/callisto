from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.messages import views as message_views

from callisto.auth_app.forms import AppUserRegistrationForm


class AppUserRegistrationView(views.CreateView, message_views.SuccessMessageMixin):
    form_class = AppUserRegistrationForm
    template_name = 'auth/register.html'
    success_message = "Account successfully created!"  # TODO - not working -> base.html; messages
    success_url = reverse_lazy('blog')  # TODO - auto login after reg


class AppUserLoginView(auth_views.LoginView, message_views.SuccessMessageMixin):
    template_name = 'auth/login.html'
    success_message = "Successfully logged in!"  # TODO - not working -> base.html; messages

    def get_success_url(self):  # TODO - if ?next=... -> redirect there
        return reverse_lazy('blog')


class AppUserLogoutView(auth_views.LogoutView, message_views.SuccessMessageMixin):
    template_name = 'auth/logout.html'
    success_message = "You have been logged out!"  # TODO - not working -> base.html; messages
