from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from callisto.users_app.models import AppUser

UserModel = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    date_posted = models.DateTimeField(
        default=timezone.now,
    )

    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
