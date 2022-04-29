from django.db import models
from PIL import Image

from callisto.auth_app.models import AppUser


class Profile(models.Model):  # TODO - image name -> f'{user.email}...'
    profile_picture = models.ImageField(
        default='default.jpg',
        upload_to='profile_pics'
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
    )

    def save(  # TODO -> return super().save()...
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        """
        Reduces the size of the photo => fewer data used
        """
        super().save()
        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)

    def __str__(self):
        return f'{self.user.email} Profile'
