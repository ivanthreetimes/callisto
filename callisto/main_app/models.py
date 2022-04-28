from django.db import models
from django.utils import timezone

from callisto.auth_app.models import AppUser


class Post(models.Model):
    title = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    date_posted = models.DateTimeField(
        default=timezone.now,
    )

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    # last_modified = models.DateTimeField(
    #     auto_now=True
    # )
