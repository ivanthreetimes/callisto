from django.urls import path

from callisto.auth_app.views import AppUserRegistrationView, AppUserLoginView, AppUserLogoutView

urlpatterns = [
    path('register/', AppUserRegistrationView.as_view(), name='user register'),
    path('login/', AppUserLoginView.as_view(), name='user login'),
    path('logout/', AppUserLogoutView.as_view(), name='user logout'),
]
