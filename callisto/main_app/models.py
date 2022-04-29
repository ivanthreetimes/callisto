from django.db import models
from django.urls import reverse
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

    # TODO
    # last_modified = models.DateTimeField(
    #     auto_now=True
    # )

    def get_absolute_url(self):
        """
        Redirects to post/<int:pk>/ after successful creation of a post
        """
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
