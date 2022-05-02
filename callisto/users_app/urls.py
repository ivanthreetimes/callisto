from django.contrib.auth import views as auth_views
from django.urls import path

from callisto.users_app.views import AppUserRegistrationView, AppUserLoginView, AppUserLogoutView

urlpatterns = [
    path('login/', AppUserLoginView.as_view(), name='user login'),
    path('logout/', AppUserLogoutView.as_view(), name='user logout'),
    path('register/', AppUserRegistrationView.as_view(), name='user register'),
]
