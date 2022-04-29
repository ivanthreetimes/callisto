from django.contrib import admin

from callisto.main_app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
