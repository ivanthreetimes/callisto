from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('callisto.main_app.urls')),
    path('auth/', include('callisto.auth_app.urls')),
    path('admin/', admin.site.urls),
]
