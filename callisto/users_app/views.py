from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login
from django.contrib.messages import views as message_views

from callisto.users_app.forms import AppUserRegistrationForm


class AppUserRegistrationView(views.CreateView, message_views.SuccessMessageMixin):
    form_class = AppUserRegistrationForm
    template_name = 'auth/register.html'
    success_message = "Account successfully created!"  # TODO - success_message not working
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class AppUserLoginView(auth_views.LoginView, message_views.SuccessMessageMixin):
    template_name = 'auth/login.html'
    success_message = "Successfully logged in!"  # TODO - success_message not working

    def get_success_url(self):
        return reverse_lazy('blog')


class AppUserLogoutView(auth_views.LogoutView, message_views.SuccessMessageMixin):
    template_name = 'auth/logout.html'
    success_message = "You have been logged out!"  # TODO - success_message not working
