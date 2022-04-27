from django.urls import path
from django.views import generic as views

from callisto.auth_app.views import AppUserRegistrationView, AppUserLoginView, AppUserLogoutView

urlpatterns = [
    path('', views.TemplateView.as_view(template_name='index.html'))
]
