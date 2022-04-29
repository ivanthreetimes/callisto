from django.urls import path

from callisto.users_app.views import profile

urlpatterns = [
    path('', profile, name='user profile'),
]
