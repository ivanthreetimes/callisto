from django.contrib import admin

from callisto.main_app.models import Post
from callisto.main_app.models import Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
