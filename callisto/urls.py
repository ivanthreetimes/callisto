from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [  # TODO - custom 403(forbidden), 404 pages
    path('', include('callisto.main_app.urls')),
    path('auth/', include('callisto.auth_app.urls')),
    path('users/', include('callisto.users_app.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
